# Generated by Django 4.1.5 on 2023-03-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0005_alter_student_comment_alter_student_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='financing_form',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profcard',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_book',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]