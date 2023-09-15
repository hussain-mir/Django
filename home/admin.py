from django.contrib import admin

# Register your models here.
from home.models import Blog,Contect
class BlogAdmin(admin.ModelAdmin):
    class Media:
        
        css={
            "all":("css/main.css",) 
        }
        
        js=("js/blog.js",)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Contect)