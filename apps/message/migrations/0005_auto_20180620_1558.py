# Generated by Django 2.0.5 on 2018-06-20 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20180502_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessgae',
            options={'ordering': ['-object_id'], 'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
    ]
