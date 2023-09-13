# Generated by Django 4.2.5 on 2023-09-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_order_status_alter_order_status_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'ordering': ('id',), 'verbose_name': 'Bot user', 'verbose_name_plural': 'Bot users'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('id',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderfile',
            options={'ordering': ('id',), 'verbose_name': 'Order file', 'verbose_name_plural': 'Order files'},
        ),
        migrations.AlterModelOptions(
            name='orderhistory',
            options={'ordering': ('id',), 'verbose_name': 'Order history', 'verbose_name_plural': 'Order histories'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('id',), 'verbose_name': 'Order item', 'verbose_name_plural': 'Order items'},
        ),
        migrations.AlterModelOptions(
            name='paymenthistory',
            options={'ordering': ('id',), 'verbose_name': 'Payment history', 'verbose_name_plural': 'Payment histories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('id',), 'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AddField(
            model_name='botuser',
            name='language',
            field=models.CharField(choices=[('uz', "O'zbek"), ('ru', 'Русский'), ('en', 'English')], default='uz', help_text='Language of user', max_length=2, verbose_name='Language'),
        ),
    ]
