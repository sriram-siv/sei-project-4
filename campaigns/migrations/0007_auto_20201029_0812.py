# Generated by Django 3.1.2 on 2020-10-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0006_campaign_coordinators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
