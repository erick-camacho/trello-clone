# Generated by Django 2.2.17 on 2020-12-16 19:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='members',
            field=models.ManyToManyField(related_name='card_members', to=settings.AUTH_USER_MODEL),
        ),
    ]