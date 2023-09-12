from modeltranslation.translator import translator, TranslationOptions
from .models import Order, OrderHistory, OrderFile, Comment, Category, Subcategory, BotUser

class OrderTranslationOptions(TranslationOptions):
    fields = ('description', 'status')

class OrderHistoryTranslationOptions(TranslationOptions):
    fields = ('status',)

class CommentTranslationOptions(TranslationOptions):
    fields = ('body',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Subcategory, SubcategoryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Comment, CommentTranslationOptions)
translator.register(Order, OrderTranslationOptions)
translator.register(OrderHistory, OrderHistoryTranslationOptions)

