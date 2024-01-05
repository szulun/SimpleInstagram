from django.contrib import admin
from InstaApp.models import Post, InstaUser, Like, UserConnection, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted_on')
#Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)
admin.site.register(Comment)