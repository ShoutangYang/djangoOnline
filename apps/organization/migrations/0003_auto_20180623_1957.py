# Generated by Django 2.0.5 on 2018-06-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180623_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高效')], default='培训机构', max_length=20, verbose_name='机构类别'),
        ),
    ]
