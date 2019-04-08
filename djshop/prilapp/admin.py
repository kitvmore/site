from django.contrib import admin
from .models import Tutorial


#pip install django-tinymce4-lite.
from tinymce.widgets import TinyMCE
from django.db import models



class TutorialAdmin(admin.ModelAdmin):
    #fields = ["tutorial_title",
    #          "tutorial_date",
    #          "tutorial_content" ]

    fieldsets = [
        ("Time/date",{"fields":["tutorial_title", "tutorial_date"]}),
        ("Content", {"fields":["tutorial_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Tutorial,TutorialAdmin)
# Register your models here.
