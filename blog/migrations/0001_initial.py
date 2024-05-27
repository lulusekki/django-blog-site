# Generated by Django 4.2.13 on 2024-05-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(max_length=100, unique=True, verbose_name="カテゴリ名"),
                ),
                (
                    "category_image",
                    models.ImageField(upload_to="images/", verbose_name="カテゴリ画像"),
                ),
            ],
            options={
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="タイトル")),
                ("content", models.TextField(verbose_name="内容")),
                ("postdate", models.DateField(auto_now_add=True, verbose_name="投稿日")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="blog.category",
                        verbose_name="カテゴリ",
                    ),
                ),
            ],
            options={
                "db_table": "blog",
            },
        ),
    ]
