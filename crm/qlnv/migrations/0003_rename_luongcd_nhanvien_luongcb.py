# Generated by Django 5.0 on 2023-12-24 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qlnv', '0002_alter_nhanvien_luonght'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nhanvien',
            old_name='luongCD',
            new_name='luongCB',
        ),
    ]