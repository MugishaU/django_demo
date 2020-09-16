# Generated by Django 3.1.1 on 2020-09-16 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]