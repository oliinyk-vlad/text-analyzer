from django.contrib import admin
from app.models import Text, Word


class WordInline(admin.TabularInline):
    model = Word
    extra = 0


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    inlines = [WordInline]
