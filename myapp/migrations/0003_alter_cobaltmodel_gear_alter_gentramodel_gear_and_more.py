# Generated by Django 4.2.7 on 2024-01-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_cobaltmodel_image_alter_gentramodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobaltmodel',
            name='gear',
            field=models.CharField(choices=[('Manual', 'M'), ('Auto', 'A')], max_length=9),
        ),
        migrations.AlterField(
            model_name='gentramodel',
            name='gear',
            field=models.CharField(choices=[('Manual', 'M'), ('Auto', 'A')], max_length=9),
        ),
        migrations.AlterField(
            model_name='malibumodel',
            name='gear',
            field=models.CharField(choices=[('Manual', 'M'), ('Auto', 'A')], max_length=9),
        ),
        migrations.AlterField(
            model_name='nexiamodel',
            name='gear',
            field=models.CharField(choices=[('Manual', 'M'), ('Auto', 'A')], max_length=9),
        ),
    ]