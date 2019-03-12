from django.contrib import admin
from .models import Posting
# Register your models here.

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 레코드 개별화면 확인
    list_display = ('id', 'content', 'created_at', 'updated_at') # 리스트에서 표시할 컬럼들
    list_display_links = ('id', 'content')  # list 목록에서 clickable할 속성

admin.site.register(Posting, PostingModelAdmin)