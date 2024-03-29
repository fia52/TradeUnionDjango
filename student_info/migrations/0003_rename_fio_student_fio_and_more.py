# Generated by Django 4.1.5 on 2023-03-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0002_alter_student_fio_alter_student_birthdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='FIO',
            new_name='fio',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='prof_card',
            new_name='profcard',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stud_book',
            new_name='student_book',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
