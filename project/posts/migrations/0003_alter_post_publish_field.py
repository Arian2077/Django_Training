# Generated by Django 5.1 on 2024-08-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_created_time_alter_post_publish_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_field',
            field=models.DateField(blank=True, null=True),
        ),
    ]
