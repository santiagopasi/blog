# Generated by Django 4.0.4 on 2022-06-16 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_comentarios_delete_customuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='creado_en',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creado_en', to='blogApp.post'),
        ),
    ]
