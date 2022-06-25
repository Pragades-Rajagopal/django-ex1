from django.contrib import admin
from .models import Publisher, Author, Book

admin.site.site_header = 'Mysite Administration'
admin.site.site_title = 'Mysite Admin Lounge'
admin.site.index_title = 'Mysite Admin'

class BookInline(admin.TabularInline):
    model = Book
    extra: int = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'name', 'email')
    list_display_links = ['name']

    fieldsets = [(None, {'fields': ['salutation', 'first_name', 'last_name', 'email']})]

    def name(self, instance):
        return instance.first_name + ' ' + instance.last_name


class PublisherAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'address', 'city', 'state_province', 'country', 'website']})]
    inlines = [BookInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_authors', 'publisher', 'publication_date', 'num_pages')
    actions = None
    list_display_links = ['title']
    search_fields = ['title']

    def title_authors (self, instance):
        return [author.first_name + ' ' + author.last_name for author in instance.authors.all()]

    def has_add_permission(self, request) -> bool:
        return False


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

