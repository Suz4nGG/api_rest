# Generated by Django 4.1.1 on 2022-09-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(choices=[('hp', 'HP'), ('aw', 'Alienware'), ('rz', 'Razer'), ('om', 'Omen'), ('lv', 'Lenovo'), ('dl', 'Dell')], default='Choice a mark', max_length=2)),
                ('nombre', models.CharField(max_length=200)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]