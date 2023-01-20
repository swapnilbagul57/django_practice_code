from django.contrib import admin

# Register your models here.
from .models import Member, Info
admin.site.register(Member)
admin.site.register(Info)
