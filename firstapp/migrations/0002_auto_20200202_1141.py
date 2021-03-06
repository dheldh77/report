# Generated by Django 3.0.2 on 2020-02-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='tmp1',
            new_name='cause',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='tmp2',
            new_name='fact',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='tmp3',
            new_name='fault',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='tmp4',
            new_name='line',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='tmp5',
            new_name='maker',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='measure',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='model',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='part',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='phenomenon',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
