# Generated by Django 2.1.2 on 2018-11-07 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_becario_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='becario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Becario'),
        ),
    ]