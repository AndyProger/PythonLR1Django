# Generated by Django 4.0.4 on 2022-05-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkURL', models.CharField(max_length=300, verbose_name='Link')),
                ('counter', models.IntegerField(verbose_name='Counter')),
            ],
        ),
    ]
