# Generated by Django 3.1.2 on 2020-10-13 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='numeroPagina',
            new_name='numeroPaginas',
        ),
    ]
