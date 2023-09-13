from django.db import models
from django.utils.translation import gettext_lazy as _

ORDER_STATUS = (
    ('new', _('Ko\'rib chiqilmoqda')),
    ('in_progress', _('Tayyorlanmoqda')),
    ('done', _('Tayyor')),
    ('canceled', _('Bekor qilingan')),
)

ORDER_TYPE = (
    ('OAK Jurnal', _('OAK Jurnal')),
    ('Respublika konferensiya', _('Respublika konferensiya')),
    ('Xalqaro ilmiy jurnal', _('Xalqaro ilmiy jurnal')),
    ('Xalqaro konferensiya', _('Xalqaro konferensiya')),
)

PAYMENT_PROVIDER = (
    ('click', _('Click')),
    ('payme', _('Payme')),
    ('cash', _('Naqd')),
)

LANGUAGE = (
    ('uz', _('O\'zbek')),
    ('ru', _('Русский')),
    ('en', _('English')),
)


class BotUser(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'), blank=True, null=True, help_text=_('Full name of user'))
    username = models.CharField(max_length=255, verbose_name=_('Username'), blank=True, null=True, help_text=_('Username of user'), unique=True)
    telegram_id = models.IntegerField(verbose_name=_('Telegram ID'), blank=True, null=True, help_text=_('Telegram ID of user'), unique=True)
    phone_number = models.CharField(max_length=255, verbose_name=_('Phone number'), blank=True, null=True, help_text=_('Phone number of user'))
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True, help_text=_('Email of user'))
    workplace = models.CharField(max_length=255, verbose_name=_('Workplace'), blank=True, null=True, help_text=_('Workplace of user'))
    position = models.CharField(max_length=255, verbose_name=_('Position'), blank=True, null=True, help_text=_('Position of user'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Added'), help_text=_('Date and time of user added'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'), help_text=_('Date and time of user updated'))

    language = models.CharField(max_length=2, verbose_name=_('Language'), help_text=_('Language of user'), choices=LANGUAGE, default='uz')

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('Bot user')
        verbose_name_plural = _('Bot users')
        ordering = ('-id',)
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), help_text=_('Name of category'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'), help_text=_('Slug of category'), unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # ordering by id
        ordering = ('id',)

class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), help_text=_('Name of subcategory'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'), help_text=_('Slug of subcategory'), unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'), help_text=_('Category of subcategory'))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')
        # ordering by id
        ordering = ('id',)

class Order(models.Model):
    type = models.CharField(max_length=50, verbose_name=_('Type'), help_text=_('Type of order'), choices=ORDER_TYPE, default='OAK Jurnal')
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, verbose_name=_('User'), help_text=_('User of order'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'), help_text=_('Category of order'))
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name=_('Subcategory'), help_text=_('Subcategory of order'))
    description = models.TextField(verbose_name=_('Description'), help_text=_('Description of order'))
    status = models.CharField(max_length=255, verbose_name=_('Status'), help_text=_('Status of order'), choices=ORDER_STATUS, default='new')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'), help_text=_('Date and time of order created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'), help_text=_('Date and time of order updated'))


    def __str__(self) -> str:
        return self.user.full_name
    

    @property
    def files(self):
        return OrderFile.objects.filter(order=self)
    
    @property
    def order_history(self):
        return OrderHistory.objects.filter(order=self)
    

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        # ordering by id
        ordering = ('id',)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'), help_text=_('Order of item'))
    name = models.CharField(max_length=255, verbose_name=_('Name'), help_text=_('Name of item'))
    # quantity = models.IntegerField(verbose_name=_('Quantity'), help_text=_('Quantity of item'))
    duration = models.IntegerField(verbose_name=_('Duration'), help_text=_('Duration of item'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'), help_text=_('Price of item'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'), help_text=_('Date and time of item created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'), help_text=_('Date and time of item updated'))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')
        # ordering by id
        ordering = ('id',)    


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'), help_text=_('Order of history'))
    status = models.CharField(max_length=255, verbose_name=_('Status'), help_text=_('Status of history'), choices=ORDER_STATUS, default='new')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'), help_text=_('Date and time of history created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'), help_text=_('Date and time of history updated'))

    def __str__(self) -> str:
        return self.order.user.full_name
    
    class Meta:
        verbose_name = _('Order history')
        verbose_name_plural = _('Order histories')
        # ordering by id
        ordering = ('id',)

class OrderFile(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'), help_text=_('Order of file'))
    file = models.FileField(upload_to='order_files/', verbose_name=_('File'), help_text=_('File of order'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Added'), help_text=_('Date and time of file added'))

    def __str__(self) -> str:
        return self.order.user.full_name
    
    class Meta:
        verbose_name = _('Order file')
        verbose_name_plural = _('Order files')
        # ordering by id
        ordering = ('id',)


class Comment(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, verbose_name=_('User'), help_text=_('User of comment'))
    body = models.TextField(verbose_name=_('Body'), help_text=_('Body of comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'), help_text=_('Date and time of comment created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'), help_text=_('Date and time of comment updated'))

    def __str__(self) -> str:
        return self.user.full_name
    
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        # ordering by id
        ordering = ('id',)

class PaymentHistory(models.Model):
    payment_provider = models.CharField(max_length=20, verbose_name=_('Payment provider'), help_text=_('Payment provider of payment history'), choices=PAYMENT_PROVIDER, default='click')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'), help_text=_('Order of payment history'))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Amount'), help_text=_('Amount of payment history'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'), help_text=_('Date and time of payment history created'))

    def __str__(self) -> str:
        return self.order.user.full_name
    
    class Meta:
        verbose_name = _('Payment history')
        verbose_name_plural = _('Payment histories')
        # ordering by id
        ordering = ('id',)
        
