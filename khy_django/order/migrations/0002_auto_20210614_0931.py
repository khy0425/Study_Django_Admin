# Generated by Django 3.2.3 on 2021-06-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='메모'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='대기중', max_length=32, verbose_name='상태'),
        ),
    ]
