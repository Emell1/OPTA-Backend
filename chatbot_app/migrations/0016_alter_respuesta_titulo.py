# Generated by Django 4.2.19 on 2025-04-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0015_respuesta_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='titulo',
            field=models.CharField(default='', max_length=200),
        ),
    ]
