# Generated by Django 4.2.6 on 2023-10-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_question_opt4_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]