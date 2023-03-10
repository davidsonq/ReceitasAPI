# Generated by Django 4.1.7 on 2023-02-24 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('instructions', models.TextField()),
                ('prep_time', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category')),
                ('ingredients', models.ManyToManyField(to='ingredients.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
