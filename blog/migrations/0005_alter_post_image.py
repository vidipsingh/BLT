# Generated by Django 5.1.3 on 2024-11-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_post_slug_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="blog_posts"),
        ),
    ]
