# Generated by Django 4.1.7 on 2023-03-15 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('team_pic', models.ImageField(blank=True, upload_to='team_image')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=80)),
                ('bio', models.CharField(max_length=1500)),
                ('max_ent', models.IntegerField(default=16)),
                ('open_date', models.DateTimeField()),
                ('close_date', models.DateTimeField()),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tournaments',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'competitor'), (2, 'staff'), (3, 'admin')], default=1)),
                ('pfp', models.ImageField(blank=True, upload_to='profile_images')),
                ('pronouns', models.CharField(max_length=20)),
                ('discord', models.CharField(max_length=50)),
                ('score_saber', models.URLField(blank=True)),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='SUPA_Triple_Rumble_Tournament.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_team_players', models.IntegerField(default=4)),
                ('valid_team', models.BooleanField(default=False)),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SUPA_Triple_Rumble_Tournament.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='team_captain',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_captain', to='SUPA_Triple_Rumble_Tournament.userprofile'),
        ),
        migrations.CreateModel(
            name='IndividualTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_rank', models.IntegerField(default=0)),
                ('min_rank', models.IntegerField(default=0)),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SUPA_Triple_Rumble_Tournament.tournament')),
            ],
        ),
    ]