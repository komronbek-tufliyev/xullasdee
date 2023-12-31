# Generated by Django 4.2.5 on 2023-09-09 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, help_text='Full name of user', max_length=255, null=True, verbose_name='Full name')),
                ('username', models.CharField(blank=True, help_text='Username of user', max_length=255, null=True, unique=True, verbose_name='Username')),
                ('telegram_id', models.IntegerField(blank=True, help_text='Telegram ID of user', null=True, unique=True, verbose_name='Telegram ID')),
                ('phone_number', models.CharField(blank=True, help_text='Phone number of user', max_length=255, null=True, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, help_text='Email of user', max_length=254, null=True, verbose_name='Email')),
                ('added', models.DateTimeField(auto_now_add=True, help_text='Date and time of user added', verbose_name='Added')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time of user updated', verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Bot user',
                'verbose_name_plural': 'Bot users',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of category', max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Slug of category', max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Description of order', verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time of order created', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time of order updated', verbose_name='Updated')),
                ('category', models.ForeignKey(help_text='Category of order', on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of subcategory', max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Slug of subcategory', max_length=255, unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(help_text='Category of subcategory', on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OrderFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='File of order', upload_to='order_files/', verbose_name='File')),
                ('added', models.DateTimeField(auto_now_add=True, help_text='Date and time of file added', verbose_name='Added')),
                ('order', models.ForeignKey(help_text='Order of file', on_delete=django.db.models.deletion.CASCADE, to='app.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order file',
                'verbose_name_plural': 'Order files',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='subcategory',
            field=models.ForeignKey(help_text='Subcategory of order', on_delete=django.db.models.deletion.CASCADE, to='app.subcategory', verbose_name='Subcategory'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(help_text='User of order', on_delete=django.db.models.deletion.CASCADE, to='app.botuser', verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(help_text='Body of comment', verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of comment created', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of comment updated', verbose_name='Updated at')),
                ('user', models.ForeignKey(help_text='User of comment', on_delete=django.db.models.deletion.CASCADE, to='app.botuser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-id',),
            },
        ),
    ]
