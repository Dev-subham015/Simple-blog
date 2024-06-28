from django.contrib import admin
from django import forms
from .models import BlogPost, Category

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    list_display = ('title', 'author', 'created_at', 'updated_at', 'category')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'updated_at', 'category')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
