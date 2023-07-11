# Generated by Django 4.2.3 on 2023-07-11 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quill_scope_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quill_scope_app.topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
