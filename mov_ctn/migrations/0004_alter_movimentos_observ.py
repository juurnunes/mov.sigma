# Generated by Django 4.1.5 on 2023-01-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov_ctn', '0003_alter_movimentos_observ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentos',
            name='observ',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
