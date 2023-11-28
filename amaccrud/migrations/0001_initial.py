# Generated by Django 3.0.5 on 2023-11-20 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
                ('objetivo', models.CharField(max_length=255)),
                ('formato', models.CharField(max_length=255)),
                ('cant_hombres', models.IntegerField()),
                ('cant_mujeres', models.IntegerField()),
                ('lugar', models.CharField(max_length=255)),
                ('dirigido', models.CharField(max_length=255)),
                ('responsable', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'metas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'temas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
                ('apoyo', models.CharField(max_length=255)),
                ('cant_hombres', models.IntegerField()),
                ('cant_mujeres', models.IntegerField()),
                ('lugar', models.CharField(max_length=255)),
                ('dirigido', models.CharField(max_length=255)),
                ('responsable', models.CharField(max_length=255)),
                ('colonia', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('meta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='amaccrud.MetaModelo')),
            ],
            options={
                'db_table': 'eventos',
                'ordering': ['-id'],
            },
        ),
    ]