# Generated by Django 4.2.19 on 2025-04-21 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'verbose_name': '6. Documento', 'verbose_name_plural': '6. Documentos'},
        ),
        migrations.AlterModelOptions(
            name='momento',
            options={'verbose_name': '3. Item', 'verbose_name_plural': '3. Items'},
        ),
        migrations.AlterModelOptions(
            name='programa',
            options={'verbose_name': '2. Grupo', 'verbose_name_plural': '2. Grupos'},
        ),
        migrations.AlterModelOptions(
            name='respuesta',
            options={'verbose_name': '5. Respuesta', 'verbose_name_plural': '5. Respuestas'},
        ),
        migrations.AlterModelOptions(
            name='submomento',
            options={'verbose_name': '4. Subitem', 'verbose_name_plural': '4. Subitems'},
        ),
        migrations.AlterModelOptions(
            name='tipolead',
            options={'verbose_name': '1. Categoría', 'verbose_name_plural': '1. Categorías'},
        ),
        migrations.AlterField(
            model_name='momento',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.programa', verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='tipo_lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.tipolead', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='process.documento', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='submomento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.submomento', verbose_name='Subitem'),
        ),
        migrations.AlterField(
            model_name='submomento',
            name='momento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.momento', verbose_name='Item'),
        ),
    ]
