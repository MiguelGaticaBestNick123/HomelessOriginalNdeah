# Generated by Django 4.2.2 on 2023-07-05 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Aportador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('nro_tarjeta', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CompraInsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('proveedor', models.CharField(max_length=40)),
                ('costo_unitario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('rut', models.CharField(error_messages='Debe ingresar rut', max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('f_nacimiento', models.DateField()),
                ('n_telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('rut', models.CharField(error_messages='Debe ingresar rut', max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('f_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=1)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.familiar')),
            ],
        ),
        migrations.CreateModel(
            name='StockInsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_stock', models.IntegerField()),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.insumo')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='comprainsumo',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.insumo'),
        ),
        migrations.AddField(
            model_name='accion',
            name='residente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.residente'),
        ),
    ]
