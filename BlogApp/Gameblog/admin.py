from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('Post_Title', 'Auther', 'Post_Date')
    search_fields = ('Post_Title', 'Auther')
admin.site.register(Post)

# Register your models here.