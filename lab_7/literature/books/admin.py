from django.contrib import admin

# Register your models here.

from .models import Book
from .models import Author
from .models import Comments

class BooksInstanceInline(admin.TabularInline):
    model=Comments

class BookModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__','year_of_pub']
    search_fields = ['title','content']
    list_display_links =['year_of_pub']
    list_filter = ['year_of_pub']
    #list_editable =['title']

    exclude=('likes',)
    inlines = [BooksInstanceInline]
    class Meta:
        model=Book

class AuthorModelAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'second_name','email']
    search_fields = ['first_name', 'second_name']
    list_display_links =['first_name', 'second_name']
    list_filter = ['first_name', 'second_name']
    list_editable = ['email']
    fields = ('first_name', 'second_name','email')

    class Meta:
        model = Author

class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['comment_text', 'comment_article']
    search_fields = ['comment_text', 'comment_article']
    list_display_links =['comment_text', 'comment_article']

    exclude = ('likes',)
    class Meta:
        model = Comments


admin.site.register(Book,BookModelAdmin)
admin.site.register(Author,AuthorModelAdmin)
admin.site.register(Comments,CommentsModelAdmin)