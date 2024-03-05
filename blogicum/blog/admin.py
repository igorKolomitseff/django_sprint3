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
        'display_category',
        'pub_date'
    )
    list_select_related = ('author', 'category', 'location')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('category__title',)
    list_display_links = ('title',)

    @admin.display(ordering='category__title', description='Категория')
    def display_category(self, obj):
        return obj.category.title


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
