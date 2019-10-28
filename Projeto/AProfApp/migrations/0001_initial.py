# Generated by Django 2.2.6 on 2019-10-25 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('carga_horaria', models.SmallIntegerField(verbose_name='Carga horária')),
                ('emenda', models.TextField(verbose_name='Emenda do curso')),
                ('valor', models.PositiveIntegerField(verbose_name='Valor(R$)')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('valor_hora_aula', models.PositiveIntegerField(verbose_name='Valor da hora aula (R$)')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AProfApp.Curso')),
            ],
            options={
                'verbose_name_plural': 'professores',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de início')),
                ('data_termino', models.DateField(verbose_name='Data de termino')),
                ('hora_inicio', models.TimeField(verbose_name='Começa à(s)')),
                ('hora_final', models.TimeField(verbose_name='Termina à(s)')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AProfApp.Professor')),
            ],
        ),
    ]
