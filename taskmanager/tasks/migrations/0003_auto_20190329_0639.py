# Generated by Django 2.1.5 on 2019-03-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Done', 'Done')], max_length=1),
        ),
    ]
