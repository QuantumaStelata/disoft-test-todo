# Generated by Django 4.1.6 on 2023-02-08 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_taskcomment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskimage',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='todo.task'),
            preserve_default=False,
        ),
    ]
