# Generated by Django 4.2.4 on 2023-08-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenAssembly',
            fields=[
                ('assembly_price', models.IntegerField()),
                ('size', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'gen_assembly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GenPack',
            fields=[
                ('pack_price', models.IntegerField()),
                ('size', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'gen_pack',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HighAssembly',
            fields=[
                ('assembly_price', models.IntegerField()),
                ('size', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'high_assembly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HighPack',
            fields=[
                ('pack_price', models.IntegerField()),
                ('size', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'high_pack',
                'managed': False,
            },
        ),
    ]
