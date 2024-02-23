from django.contrib import admin
from .models import Member

admin.site.register(Member)


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined date")
  
