from django.contrib import admin
from .models import Bbs, Bbs_user, Comment, Category

admin.site.register(Bbs)
admin.site.register(Bbs_user)
admin.site.register(Comment)
admin.site.register(Category)