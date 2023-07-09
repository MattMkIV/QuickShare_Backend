# Generated by Django 4.1.3 on 2023-06-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickshare_api', '0005_alter_note_note_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canaccesslist',
            name='fk_list',
        ),
        migrations.RemoveField(
            model_name='canaccesslist',
            name='fk_user',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='fk_financial',
        ),
        migrations.RemoveField(
            model_name='income',
            name='fk_financial',
        ),
        migrations.RemoveField(
            model_name='list',
            name='fk_user',
        ),
        migrations.RemoveField(
            model_name='listelement',
            name='fk_list',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='calendar_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='CanAccessFinancialTracker',
        ),
        migrations.DeleteModel(
            name='CanAccessList',
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
        migrations.DeleteModel(
            name='FinancialTracker',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='ListElement',
        ),
    ]
