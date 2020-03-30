# Generated by Django 3.0.4 on 2020-03-28 14:13

from django.db import migrations
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='players',
            old_name='player',
            new_name='username',
        ),

        migrations.CreateModel(
        name='Tasks',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('title', models.CharField(max_length=100)),
            ('description', models.CharField(max_length=200)),
            ('author', models.CharField(max_length=50)),
            ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]