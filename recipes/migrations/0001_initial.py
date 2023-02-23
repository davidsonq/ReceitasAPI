# Generated by Django 4.1.7 on 2023-02-23 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('instructions', models.TextField()),
                ('prep_time', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category')),
                ('ingredients', models.ManyToManyField(to='ingredients.ingredient')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
