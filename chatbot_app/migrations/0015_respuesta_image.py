# Generated by Django 4.2.19 on 2025-03-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0014_alter_respuesta_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='respuestas/'),
        ),
    ]
