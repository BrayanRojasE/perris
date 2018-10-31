# Generated by Django 2.1.2 on 2018-10-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.EmailField(max_length=254)),
                ('Rut', models.CharField(max_length=9)),
                ('NombreCompleto', models.CharField(max_length=30)),
                ('FechaNacimiento', models.DateField()),
                ('Telefono', models.IntegerField()),
                ('Region', models.IntegerField()),
                ('Ciudad', models.IntegerField()),
                ('TipoVivienda', models.CharField(choices=[('casa2', 'Casa con patio Grande'), ('casa3', 'Casa con patio pequeño'), ('casa4', 'Casa sin patio'), ('casa5', 'Departamento')], default='casa2', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroRescatados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Fotografia', models.ImageField(upload_to='')),
                ('RazaPredominante', models.CharField(max_length=20)),
                ('Descripcion', models.TextField()),
                ('Estado', models.CharField(choices=[('R', 'Rescatados'), ('D', 'Disponible'), ('A', 'Adoptado')], default='R', max_length=1)),
            ],
        ),
    ]