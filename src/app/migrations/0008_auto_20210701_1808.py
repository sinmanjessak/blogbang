# Generated by Django 3.1.7 on 2021-07-01 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20210701_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='view_count',
        ),
        migrations.CreateModel(
            name='Postview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.postmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
