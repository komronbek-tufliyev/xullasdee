
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_botuser_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'ordering': ('-id',), 'verbose_name': 'Bot user', 'verbose_name_plural': 'Bot users'},
        ),
    ]
