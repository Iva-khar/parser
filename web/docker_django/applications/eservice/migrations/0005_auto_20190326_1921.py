# Generated by Django 2.0.9 on 2019-03-26 19:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eservice', '0004_eservicesign'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eservicesign',
            unique_together={('eservice', 'user')},
        ),
    ]
