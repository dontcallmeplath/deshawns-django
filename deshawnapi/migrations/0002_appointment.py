# Generated by Django 4.2.7 on 2023-11-07 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deshawnapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='deshawnapi.walker')),
            ],
        ),
    ]
