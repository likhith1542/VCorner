from django.contrib import admin
from .models import jrny

# Register your models here.

class Jrnys(admin.ModelAdmin):
    list_display = (
        'start',
        'destination',
        'date',
        'time',
        'number',
    )


admin.site.register(jrny, Jrnys)
