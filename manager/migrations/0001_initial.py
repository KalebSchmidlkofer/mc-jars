# Generated by Django 5.0.4 on 2024-04-30 02:35

import django.db.models.deletion
import manager.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50, unique=True)),
                ('type', models.CharField(choices=[('Servers', 'Servers'), ('Proxies', 'Proxies'), ('Modded', 'Modded'), ('Vanilla', 'Vanilla'), ('Bedrock', 'Bedrock')], max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('software', models.CharField(choices=[('Vanilla', 'Vanilla'), ('Paper', 'Paper'), ('Purpur', 'Purpur'), ('Spigot', 'Spigot'), ('CraftBukkit', 'CraftBukkit'), ('Tuinity', 'Tuinity'), ('Airplane', 'Airplane'), ('Folia', 'Folia'), ('SpongeVanilla', 'SpongeVanilla'), ('Glowstone', 'Glowstone'), ('Fabric', 'Fabric'), ('Forge', 'Forge'), ('Crucible', 'Crucible'), ('Cardboard', 'Cardboard'), ('Arclight', 'Arclight'), ('Mohist', 'Mohist'), ('Magma', 'Magma'), ('SpongeForge', 'SpongeForge'), ('Waterfall', 'Waterfall'), ('Velocity', 'Velocity'), ('Bungeecord', 'Bungeecord'), ('Travertine', 'Travertine')], max_length=50)),
                ('buildnum', models.IntegerField()),
                ('posted', models.BooleanField(default=True)),
                ('file', models.FileField(upload_to=manager.models.get_upload_to)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='bedrock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bedrock', to='manager.jars')),
            ],
        ),
        migrations.CreateModel(
            name='modded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Modded', to='manager.jars')),
            ],
        ),
        migrations.CreateModel(
            name='proxies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Proxy', to='manager.jars')),
            ],
        ),
        migrations.CreateModel(
            name='servers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Server', to='manager.jars')),
            ],
        ),
        migrations.CreateModel(
            name='vanilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vanilla', to='manager.jars')),
            ],
        ),
    ]