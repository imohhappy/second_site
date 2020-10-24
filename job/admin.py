from django.contrib import admin
from .models import Vacancy, Post, Contact


class PostInline(admin.StackedInline):
    model = Post
    extra = 1


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date_pub']
    list_filter = ['date_pub']
    search_fields = ['title', 'description']
    inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'order', 'vacancy']
    list_display_links = ['name', 'description', 'order', 'vacancy']
    search_fields = ['name', 'description', 'order']
    list_filter = ['description']
    fieldsets = [
        ('name', {'fields':['name']}),
        ('description', {'fields': ['description']}),
        ('white', {'fields': ['order']}),
        (None, {'fields': ['vacancy']})
        ]


admin.site.register(Contact)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Post, PostAdmin)

# Register your models here.


