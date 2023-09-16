from django.contrib import admin

from .models import Book, Chapter, Section

admin.site.register(Book)
admin.site.register(Section)
admin.site.register(Chapter)
