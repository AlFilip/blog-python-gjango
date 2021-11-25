from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'created_at', 'update_at', 'is_published', 'category', 'get_photo')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    fields = ('title', 'content', 'category', 'is_published', 'photo', 'get_photo', 'views_count', 'created_at', 'update_at',)
    readonly_fields = ('get_photo', 'views_count', 'created_at', 'update_at',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="40">')
        return 'Нет фото'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'
