# Generated by Django 4.0.5 on 2023-05-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('idTipProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID tipo producto')),
                ('nomTipo', models.CharField(max_length=15, verbose_name='Gato Perro Exotico')),
            ],
        ),
    ]