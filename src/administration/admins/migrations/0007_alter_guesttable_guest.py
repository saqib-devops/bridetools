# Generated by Django 4.0.1 on 2023-06-04 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_alter_invitationletter_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guesttable',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_table', to='admins.guest'),
        ),
    ]
