from django.contrib import admin

from . import models


class MessageLikeInline(admin.TabularInline):
    model = models.MessageLike


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    inlines = [MessageLikeInline]
    list_display = ('author', 'content')
