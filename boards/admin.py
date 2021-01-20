from django.contrib import admin
from .models import Board, Comment


# admin 페이지 board 게시판 뷰 설정
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']


# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(Comment)
