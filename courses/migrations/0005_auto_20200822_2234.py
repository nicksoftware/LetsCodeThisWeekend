# Generated by Django 2.2.2 on 2020-08-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200719_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tutorial',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
