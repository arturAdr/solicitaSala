# Generated by Django 2.1.3 on 2018-11-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
                ('qtd_pessoas', models.IntegerField()),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sala.Sala', verbose_name='Sala')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]
