from django.contrib import admin

from .models import Mineral, Group, Category


class MineralInline(admin.StackedInline):
    model = Mineral


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MineralInline,
    ]


admin.site.register(Mineral)
admin.site.register(Category)
admin.site.register(Group, GroupAdmin)
