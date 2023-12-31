# Generated by Django 4.2.2 on 2023-06-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=3)),
                ('sexo', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1, null=True)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
