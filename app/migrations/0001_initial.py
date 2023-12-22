# Generated by Django 4.0.4 on 2023-12-22 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='', max_length=50)),
                ('father_name', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(default='', max_length=50)),
                ('course_name', models.CharField(default='', max_length=50)),
                ('cradit_hr', models.CharField(default='', max_length=50)),
                ('student_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentinfo')),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('postal', models.CharField(default='', max_length=50)),
                ('student_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.studentinfo')),
            ],
        ),
    ]