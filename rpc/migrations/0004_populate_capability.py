# Copyright The IETF Trust 2023-2025, All Rights Reserved

from django.db import migrations


def forward(apps, schema_editor):
    Capability = apps.get_model("rpc", "Capability")
    Capability.objects.create(slug="bis", name="bis", desc="Can edit a -bis RFC")
    Capability.objects.create(
        slug="clusters-beginner",
        name="Clusters: beginner",
        desc="New to working with RFC clusters",
    )
    Capability.objects.create(
        slug="clusters-intermediate",
        name="Clusters: intermediate",
        desc="Moderate experience working with RFC clusters",
    )
    Capability.objects.create(
        slug="clusters-expert",
        name="Clusters: expert",
        desc="Extensive experience working with RFC clusters",
    )
    Capability.objects.create(
        slug="codecomp-abnf",
        name="Code components: ABNF",
        desc="Can work on ABNF components",
    )
    Capability.objects.create(
        slug="codecomp-mib",
        name="Code components: MIB",
        desc="Can work on MIB components",
    )
    Capability.objects.create(
        slug="codecomp-xml",
        name="Code components: XML",
        desc="Can work on XML components",
    )
    Capability.objects.create(
        slug="codecomp-yang",
        name="Code components: YANG",
        desc="Can work on YANG components",
    )
    Capability.objects.create(
        slug="ianaconsid-beginner",
        name="IANA considerations: beginner",
        desc="New to IANA considerations",
    )
    Capability.objects.create(
        slug="ianaconsid-intermediate",
        name="IANA considerations: intermediate",
        desc="Moderate experience with IANA considerations",
    )
    Capability.objects.create(
        slug="ianaconsid-expert",
        name="IANA considerations: expert",
        desc="Extensive experience with IANA considerations",
    )
    Capability.objects.create(
        slug="statuschange",
        name="Status change",
        desc="Can oversee an RFC status change",
    )
    Capability.objects.create(
        slug="xmlv3conversion",
        name="Conversion to v3 XML",
        desc="Can convert v2 XML to v3 XML",
    )
    Capability.objects.create(
        slug="xmlfmt-beginner",
        name="XML formatting: beginner",
        desc="New to XML formatting",
    )
    Capability.objects.create(
        slug="xmlfmt-intermediate",
        name="XML formatting: intermediate",
        desc="Moderate experience with XML formatting",
    )
    Capability.objects.create(
        slug="xmlfmt-expert",
        name="XML formatting: expert",
        desc="Extensive experience with XML formatting",
    )
    Capability.objects.create(
        slug="expedite", name="Expedite", desc="Can edit an expedited RFC"
    )


def reverse(apps, schema_editor):
    Capability = apps.get_model("rpc", "Capability")
    Capability.objects.filter(
        slug__in=[
            "bis",
            "clusters-beginner",
            "clusters-intermediate",
            "clusters-expert",
            "codecomp-abnf",
            "codecomp-mib",
            "codecomp-xml",
            "codecomp-yang",
            "ianaconsid-beginner",
            "ianaconsid-intermediate",
            "ianaconsid-expert",
            "statuschange",
            "xmlv3conversion",
            "xmlfmt-beginner",
            "xmlfmt-intermediate",
            "xmlfmt-expert",
            "expedite",
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("rpc", "0003_populate_rpcrole"),
    ]

    operations = [migrations.RunPython(forward, reverse)]
