# Generated by Django 2.0.5 on 2018-05-02 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20180502_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessgae',
            options={'ordering': ['-object_id'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]