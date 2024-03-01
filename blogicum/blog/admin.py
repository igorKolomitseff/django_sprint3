from django.contrib import admin

from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = ('title',)


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'author',
        'category',
        'pub_date'
    )
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
