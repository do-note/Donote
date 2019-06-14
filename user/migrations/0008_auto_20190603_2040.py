# Generated by Django 2.2.1 on 2019-06-03 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190603_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(on_delete=False, to='user.Department', verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.ForeignKey(on_delete=False, to='user.Title', verbose_name='职位'),
        ),
    ]
