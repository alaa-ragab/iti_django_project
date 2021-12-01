# Generated by Django 3.2.9 on 2021-12-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0003_auto_20211130_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(choices=[('tag1', 'tag1'), ('tag2', 'tag2'), ('tag3', 'tag3'), ('tag4', 'tag4'), ('tag5', 'tag5'), ('tag6', 'tag6')], to='addproject.ProjectsTags'),
        ),
        migrations.AlterField(
            model_name='projectstags',
            name='tags',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]