import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example", "0003_polymorphics"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthorType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ("id",)},
        ),
        migrations.AlterModelOptions(
            name="authorbio",
            options={"ordering": ("id",)},
        ),
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ("id",)},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("id",)},
        ),
        migrations.AlterModelOptions(
            name="entry",
            options={"ordering": ("id",)},
        ),
        migrations.AlterModelOptions(
            name="taggeditem",
            options={"ordering": ("id",)},
        ),
        migrations.AlterField(
            model_name="entry",
            name="authors",
            field=models.ManyToManyField(related_name="entries", to="example.Author"),
        ),
        migrations.AddField(
            model_name="author",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="example.AuthorType",
            ),
        ),
    ]
