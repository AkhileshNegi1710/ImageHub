# Generated by Django 3.1.4 on 2021-01-10 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='productimage',
            new_name='productname',
        ),
    ]
