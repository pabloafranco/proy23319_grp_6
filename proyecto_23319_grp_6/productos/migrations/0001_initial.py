# Generated by Django 3.2.18 on 2023-05-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_clasificacion', models.CharField(max_length=100, verbose_name='Clasificacion')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de alta')),
            ],
            options={
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('provincia', models.CharField(max_length=50, verbose_name='Provincia')),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('codigo_postal', models.CharField(max_length=10, verbose_name='CodigoPostal')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('foto', models.ImageField(null=True, upload_to='perfiles/', verbose_name='Foto Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_producto', models.CharField(max_length=100, verbose_name='Descripcion Producto')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo'), ('P', 'Pausado')], default='A', max_length=1)),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('foto', models.ImageField(null=True, upload_to='image/', verbose_name='Foto Producto')),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.clasificacion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.persona')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Det_Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Cab_Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.persona')),
            ],
        ),
    ]
