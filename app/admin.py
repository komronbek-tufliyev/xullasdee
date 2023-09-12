from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from .models import *
from .translation import *



admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.

class OrderFileInline(admin.TabularInline):
    model = OrderFile
    extra = 0

class OrderHistoryInline(admin.TabularInline):
    model = OrderHistory    
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'telegram_id', 'phone_number', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('full_name', 'username', 'telegram_id', 'phone_number', 'email')
    inlines = (OrderInline,)
    fieldsets = (
        (_('User'), {
            'fields': ('full_name', 'username', 'telegram_id', 'phone_number', 'email')
        }),
        # (_('Date and time'), {
        #     'fields': ('created_at', 'updated_at')
        # }),
    )

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = (OrderInline,)
    fieldsets = (
        (_('Category'), {
            'fields': ('name', 'slug')
        }),
    )

@admin.register(Subcategory)
class SubcategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    inlines = (OrderInline,)
    fieldsets = (
        (_('Subcategory'), {
            'fields': ('name', 'slug', 'category')
        }),
    )

@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('user', 'category', 'subcategory', 'status', 'created_at', 'updated_at')
    list_filter = ('category', 'subcategory', 'status', 'created_at', 'updated_at')
    search_fields = ('user', 'category', 'subcategory', 'status')
    inlines = (OrderFileInline, OrderHistoryInline,)
    fieldsets = (
        (_('Order'), {
            'fields': ('user', 'category', 'subcategory', 'description', 'status')
        }),
        # (_('Date and time'), {
        #     'fields': ('created_at', 'updated_at')
        # }),
    )

@admin.register(OrderFile)
class OrderFileAdmin(admin.ModelAdmin):
    list_display = ('order', 'file', 'created_at')
    list_filter = ('order', 'created_at')
    search_fields = ('order', 'file')
    fieldsets = (
        (_('Order file'), {
            'fields': ('order', 'file')
        }),
        # (_('Date and time'), {
        #     'fields': ('created_at',)
        # }),
    )

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'created_at', 'updated_at')
    list_filter = ('order', 'status', 'created_at', 'updated_at')
    search_fields = ('order', 'status')
    fieldsets = (
        (_('Order history'), {
            'fields': ('order', 'status')
        }),
        # (_('Date and time'), {
        #     'fields': ('created_at', 'updated_at')
        # }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user', 'body')
    fieldsets = (
        (_('Comment'), {
            'fields': ('user', 'body')
        }),
        # (_('Date and time'), {
        #     'fields': ('created_at',)
        # }),
    )




