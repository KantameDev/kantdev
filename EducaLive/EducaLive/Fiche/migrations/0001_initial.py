# Generated by Django 4.1.7 on 2023-05-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecon', models.CharField(max_length=200, null=True)),
                ('theme', models.CharField(choices=[('Calcul numerique', 'Calcul numérique'), ('Application du plan', 'Application du plan'), ('Configuration du plan', 'Configuration du plan'), ('Organisation de données', 'Organisation de données')], max_length=200, null=True)),
                ('niveau', models.CharField(choices=[('Sixième', 'Sixième'), ('Cinquième', 'Cinquième'), ('Quatrième', 'Quatrième'), ('Troisième', 'Troisième')], max_length=200, null=True)),
                ('fiche', models.FileField(upload_to='fiches/')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
