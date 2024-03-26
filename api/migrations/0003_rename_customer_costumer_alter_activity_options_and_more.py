# Generated by Django 5.0.3 on 2024-03-24 17:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_activitycategory_alter_review_rating_activity_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Customer",
            new_name="Costumer",
        ),
        migrations.AlterModelOptions(
            name="activity",
            options={"verbose_name_plural": "Activities"},
        ),
        migrations.AlterModelOptions(
            name="activitycategory",
            options={"verbose_name_plural": "Activity Categories"},
        ),
        migrations.AlterModelOptions(
            name="activityimage",
            options={"verbose_name_plural": "Activity Images"},
        ),
        migrations.AlterModelOptions(
            name="countryimage",
            options={"verbose_name_plural": "Country Images"},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"ordering": ["-created_at"], "verbose_name_plural": "Reviews"},
        ),
    ]
