# Generated by Django 2.2.1 on 2019-05-24 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('status', models.CharField(choices=[('INA', 'Inactivo'), ('ACT', 'Activo')], default='ACT', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('status', models.CharField(choices=[('INA', 'Inactivo'), ('ACT', 'Activo')], default='ACT', max_length=3)),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('status', models.CharField(choices=[('INA', 'Inactivo'), ('ACT', 'Activo')], default='ACT', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('status', models.CharField(choices=[('INA', 'Inactivo'), ('ACT', 'Activo')], default='ACT', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('status', models.CharField(choices=[('INA', 'Inactivo'), ('ACT', 'Activo')], default='ACT', max_length=3)),
                ('modelo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=256)),
                ('internalCode', models.CharField(default=None, max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('principalCode', models.CharField(default=None, max_length=10)),
                ('image_url', models.CharField(default=None, max_length=256)),
                ('model', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Modelo')),
                ('size', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Size')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='typeProduct',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Type'),
        ),
    ]
