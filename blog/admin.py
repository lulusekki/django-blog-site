from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog


class BlogAdmin(admin.ModelAdmin):
   list_display=('id','title', 'postdate','category')

#ここから下を追加
class CategoryAdmin(admin.ModelAdmin):
   list_display=('id','category_name')
#ここまでを追加

admin.site.register(Category, CategoryAdmin)#修正
admin.site.register(Blog, BlogAdmin) 
