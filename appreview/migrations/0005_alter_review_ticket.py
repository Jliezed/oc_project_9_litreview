# Generated by Django 4.1 on 2022-09-19 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("appreview", "0004_alter_review_ticket_alter_ticket_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="appreview.ticket"
            ),
        ),
    ]