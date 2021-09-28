from django.contrib import admin
from .models import Comment,ModernBlogs,News,UserIp
# Register your models here.
admin.site.register(Comment)
admin.site.register(ModernBlogs)
admin.site.register(News)
admin.site.register(UserIp)