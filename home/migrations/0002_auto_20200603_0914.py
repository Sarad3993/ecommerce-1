# Generated by Django 3.0.6 on 2020-06-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('contact_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('', 'Default')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('image', models.TextField()),
                ('labels', models.CharField(blank=True, choices=[('special', 'special'), ('', 'Non Special')], max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='labels',
            field=models.CharField(blank=True, choices=[('special', 'special'), ('', 'Non Special')], max_length=300),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.CharField(default='product', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('', 'Default')], max_length=50),
        ),
    ]
