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
    list_display = ('telegram_id', 'username', 'language', 'full_name', 'phone_number', 'email', 'workplace', 'position',)
    list_filter = ('created_at', 'updated_at')
    search_fields = ('full_name', 'username', 'telegram_id', 'phone_number', 'workplace', 'position',)
    inlines = (OrderInline,)
    fieldsets = (
        (_('User'), {
            'fields': ('full_name', 'username', 'language', 'telegram_id', 'phone_number', 'email', 'workplace', 'position',)
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
    list_display = ('type', 'user', 'category', 'subcategory', 'status', 'created_at', 'updated_at')
    list_filter = ('category', 'subcategory', 'status', 'created_at', 'updated_at')
    search_fields = ('type', 'user', 'category', 'subcategory', 'status')
    inlines = (OrderFileInline, OrderHistoryInline,)
    fieldsets = (
        (_('Order'), {
            'fields': ('type', 'user', 'category', 'subcategory', 'description', 'status')
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

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'price', 'duration',)
    search_fields = ('order', 'name', 'price', 'duration',)
    list_filter = ('order',)
    fieldsets = (
        (_('Order item'), {
            'fields': ('order', 'name', 'price', 'duration',)
        }),
    )

@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_provider',)
    search_fields = ('order', 'amount', 'payment_provider',)
    list_filter = ('order', 'payment_provider',)
    fieldsets = (
        (_('Payment history'), {
            'fields': ('order', 'amount', 'payment_provider',)
        }),
    )




