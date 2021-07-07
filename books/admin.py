from django.contrib import admin
from .models import Genre,Language,Book

admin.site.register(Genre)
admin.site.register(Language)



class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','image','Author','genre','language')
admin.site.register(Book,BookAdmin)

