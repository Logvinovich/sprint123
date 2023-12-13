# Generated by Django 4.2.7 on 2023-12-06 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("perevalapp", "0006_alter_images_pereval_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="images",
            name="pereval_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image",
                to="perevalapp.perevaladd",
            ),
        ),
    ]
