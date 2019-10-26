# Generated by Django 2.1 on 2019-10-26 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('count', models.IntegerField(max_length=10)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Store')),
            ],
        ),
    ]
