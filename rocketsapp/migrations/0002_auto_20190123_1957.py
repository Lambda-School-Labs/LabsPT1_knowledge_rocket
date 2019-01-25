# Generated by Django 2.1.5 on 2019-01-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocketsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='name',
            new_name='className',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='studentEmail',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rocket',
        ),
        migrations.AddField(
            model_name='student',
            name='studentName',
            field=models.CharField(default='', max_length=100),
        ),
    ]