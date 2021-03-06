# Generated by Django 3.1.4 on 2021-07-07 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '2. Genre',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '3. Language',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='book_imgs/')),
                ('title', models.CharField(max_length=200, null=True)),
                ('Author', models.CharField(max_length=200, null=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.language')),
            ],
            options={
                'verbose_name_plural': '1. Book',
            },
        ),
    ]
