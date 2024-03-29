# Generated by Django 3.2.9 on 2021-11-28 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('etude', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membres', models.ManyToManyField(to='user.Encadreur', verbose_name='membres')),
            ],
            options={
                'verbose_name': 'Jury',
                'verbose_name_plural': 'Jurys',
            },
        ),
        migrations.CreateModel(
            name='Soutenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('lieu', models.CharField(max_length=50, verbose_name='lieu')),
                ('acces', models.CharField(max_length=50, verbose_name='acces')),
                ('rapport_soutenance', models.FileField(upload_to=None, verbose_name='rapport soutenance')),
                ('resume', models.TextField(verbose_name='resume soutenance')),
                ('jury', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='soutenance.jury', verbose_name='jury')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etude.projetfindetudes', verbose_name='PFE')),
            ],
            options={
                'verbose_name': 'Soutenance',
                'verbose_name_plural': 'Soutenances',
            },
        ),
        migrations.CreateModel(
            name='Appreciations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarques', models.CharField(max_length=500, verbose_name='remarques')),
                ('appreciations', models.CharField(max_length=100, verbose_name='appreciation')),
                ('suggestions', models.CharField(max_length=500, verbose_name='suggestions')),
                ('note', models.PositiveSmallIntegerField(verbose_name='note')),
                ('jury', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soutenance.jury', verbose_name='jury')),
                ('soutenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etude.soutenant', verbose_name='soutenant')),
            ],
            options={
                'verbose_name': 'Appreciations',
                'verbose_name_plural': 'Appreciationss',
            },
        ),
    ]
