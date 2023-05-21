# Generated by Django 4.1.5 on 2023-03-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=50)),
                ('birthdate', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('financing_form', models.CharField(max_length=50)),
                ('prof_card', models.CharField(max_length=50)),
                ('stud_book', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('tg_id', models.CharField(max_length=50)),
            ],
        ),
    ]