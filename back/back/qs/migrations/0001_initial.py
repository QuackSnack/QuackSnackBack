# Generated by Django 4.0.5 on 2022-06-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('articles', models.ManyToManyField(to='qs.article')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('role', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.IntegerField()),
                ('articles', models.ManyToManyField(to='qs.article')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qs.user')),
                ('menus', models.ManyToManyField(to='qs.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qs.user'),
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qs.user'),
        ),
    ]
