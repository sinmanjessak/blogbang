# Generated by Django 3.1.7 on 2021-06-30 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.postmodel'),
        ),
    ]
