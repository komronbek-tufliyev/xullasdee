from faker import Faker
from app.models import BotUser, Category, Comment, Order, OrderFile, OrderHistory, Subcategory
from googletrans import Translator


def translate_en_ru(text: str) -> str:
    translator = Translator()
    return translator.translate(text, dest='ru').text

def translate_en_uz(text: str) -> str:
    translator = Translator()
    return translator.translate(text, dest='uz').text

def translate_uz_ru(text: str) -> str:
    translator = Translator()
    return translator.translate(text, dest='ru').text

def translate_uz_en(text: str) -> str:
    translator = Translator()
    return translator.translate(text, dest='en').text

def generate_bot_users() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(BotUser(
            full_name=fake.name(),
            username=fake.user_name(),
            telegram_id=fake.random_int(min=100000000, max=999999999),
            phone_number=fake.phone_number(),
            email=fake.email(),
        ))
    BotUser.objects.bulk_create(data)

def generate_categories() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(Category(
            name=fake.name(),
            name_uz = translate_en_uz(fake.name()),
            name_en=fake.name(),
            name_ru=translate_en_ru(fake.name()),
            slug=fake.slug(),
        ))
    Category.objects.bulk_create(data)

def generate_subcategories() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(Subcategory(
            name=fake.name(),
            name_uz = translate_en_uz(fake.name()),
            name_en=fake.name(),
            name_ru=translate_en_ru(fake.name()),
            slug=fake.slug(),
            category=Category.objects.get(id=fake.random_int(min=1, max=100)),
        ))
    Subcategory.objects.bulk_create(data)


def generate_orders() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(Order(
            user=BotUser.objects.get(id=fake.random_int(min=1, max=100)),
            category=Category.objects.get(id=fake.random_int(min=1, max=100)),
            subcategory=Subcategory.objects.get(id=fake.random_int(min=1, max=100)),
            description=fake.text(),
            description_uz = translate_en_uz(fake.text()),
            description_en=fake.text(),
            description_ru=translate_en_ru(fake.text()),
            status=fake.random_element(elements=('new', 'in_progress', 'done', 'rejected')),
        ))
    Order.objects.bulk_create(data)

def generate_order_files() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(OrderFile(
            order=Order.objects.get(id=fake.random_int(min=1, max=100)),
            file=fake.file_name(),
        ))
    OrderFile.objects.bulk_create(data)

def generate_order_histories() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(OrderHistory(
            order=Order.objects.get(id=fake.random_int(min=1, max=100)),
            status=fake.random_element(elements=('new', 'in_progress', 'done', 'rejected')),
        ))
    OrderHistory.objects.bulk_create(data)

def generate_comments() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        data.append(Comment(
            order=Order.objects.get(id=fake.random_int(min=1, max=100)),
            body=fake.text(),
            body_uz = translate_en_uz(fake.text()),
            body_en=fake.text(),
            body_ru=translate_en_ru(fake.text()),
        ))
    Comment.objects.bulk_create(data)


def generate_fake_data() -> None:
    generate_bot_users()
    generate_categories()
    generate_subcategories()
    generate_orders()
    generate_order_files()
    generate_order_histories()
    generate_comments()

if __name__ == '__main__':
    generate_fake_data()
