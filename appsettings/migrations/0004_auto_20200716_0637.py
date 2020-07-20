# Generated by Django 2.2.13 on 2020-07-16 06:37

from django.db import migrations
from django.utils.translation import ugettext_lazy as _


def add_default_settings(apps, schema_editor):
    setting = apps.get_model("appsettings", "AppSettings")
    db_alias = schema_editor.connection.alias
    setting.objects.using(db_alias).bulk_create([
        setting(27, _("Console Scale"), "CONSOLE_SCALE", "False", "True,False", _("Allow console to scaling view")),
        setting(28, _("Console View-Only"), "CONSOLE_VIEW_ONLY", "False", "True,False", _("Allow only view not modify")),
        setting(29, _("Console Resize Session"), "CONSOLE_RESIZE_SESSION", "False", "True,False", _("Allow to resize session for console")),
        setting(30, _("Console Clip Viewport"), "CONSOLE_CLIP_VIEWPORT", "False", "True,False", _("Clip console viewport")),
    ])


def del_default_settings(apps, schema_editor):
    setting = apps.get_model("appsettings", "AppSettings")
    db_alias = schema_editor.connection.alias
    setting.objects.using(db_alias).filter(key="CONSOLE_SCALE").delete()
    setting.objects.using(db_alias).filter(key="CONSOLE_VIEW_ONLY").delete()
    setting.objects.using(db_alias).filter(key="CONSOLE_RESIZE_SESSION").delete()
    setting.objects.using(db_alias).filter(key="CONSOLE_CLIP_VIEWPORT").delete()
    

class Migration(migrations.Migration):

    dependencies = [
        ('appsettings', '0003_auto_20200615_0637'),
    ]

    operations = [
        migrations.RunPython(add_default_settings, del_default_settings),
    ]