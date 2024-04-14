# Generated by Django 4.2.11 on 2024-04-14 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='id',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='taskid',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
