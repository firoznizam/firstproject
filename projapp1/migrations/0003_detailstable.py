# Generated by Django 4.1.7 on 2023-04-19 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projapp1', '0002_doctortable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailstable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctdetails', models.CharField(max_length=200)),
                ('doctdescription', models.TextField(max_length=500)),
                ('doctimage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projapp1.doctortable')),
            ],
        ),
    ]
