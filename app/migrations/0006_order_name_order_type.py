# Generated by Django 4.2.5 on 2023-09-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_botuser_position_botuser_workplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, help_text='Name of order', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('OAK Jurnal', 'OAK Jurnal'), ('Respublika konferensiya', 'Respublika konferensiya'), ('Xalqaro ilmiy jurnal', 'Xalqaro ilmiy jurnal'), ('Xalqaro konferensiya', 'Xalqaro konferensiya')], default='OAK Jurnal', help_text='Type of order', max_length=50, verbose_name='Type'),
        ),
    ]