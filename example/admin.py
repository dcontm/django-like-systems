from django.contrib import admin
from . models import Test, Test1
# Register your models here.


class TestAdmin(admin.ModelAdmin):
    list_display = ("headline",)


class Test1Admin(admin.ModelAdmin):
    list_display = ("headline",)


admin.site.register(Test, TestAdmin)
admin.site.register(Test1, Test1Admin)
