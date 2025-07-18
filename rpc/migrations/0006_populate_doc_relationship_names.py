# Copyright The IETF Trust 2025, All Rights Reserved

from django.db import migrations


def forward(apps, schema_editor):
    DocRelationshipName = apps.get_model("rpc", "DocRelationshipName")

    DocRelationshipName.objects.create(
        slug="missref",
        name="Missing reference",
        desc="Normative reference to a document that is still in draft state",
        used=True,
    )

    DocRelationshipName.objects.create(
        slug="refqueue",
        name="Reference in Queue",
        desc="Normative reference to a document that is in queue for publication",
        used=True,
    )


def reverse(apps, schema_editor):
    DocRelationshipName = apps.get_model("rpc", "DocRelationshipName")
    DocRelationshipName.objects.filter(slug__in=["missref", "refqueue"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("rpc", "0005_populate_labels"),
    ]

    operations = [migrations.RunPython(forward, reverse)]
