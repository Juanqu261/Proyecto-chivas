# Generated by Django 4.2.4 on 2023-11-21 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_reserva', models.CharField(max_length=10)),
                ('numero_reserva', models.CharField(max_length=20)),
                ('nombre_titular', models.CharField(max_length=30)),
                ('identificacion_titular', models.CharField(max_length=15)),
            ],
        ),
    ]