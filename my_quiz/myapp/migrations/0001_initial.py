# Generated by Django 4.2.6 on 2023-10-16 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='media/image')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/image')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myapp.category')),
            ],
        ),
    ]