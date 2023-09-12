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
        print(_, "generatsiya")
        name = fake.name()
        name_uz = translate_en_uz(name)
        name_en = name
        name_ru = translate_en_ru(name)
        print(f"{_}-generatsiya: {name_uz}, {name_en}, {name_ru}")

        data.append(Category(
            name=name,
            name_uz = name_uz,
            name_en=name_en,
            name_ru=name_ru,
            slug=fake.slug(),
        ))
    Category.objects.bulk_create(data)

def generate_subcategories() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        name = fake.name()
        name_uz = translate_en_uz(name)
        name_en = name
        name_ru = translate_en_ru(name)

        data.append(Subcategory(
            name=name,
            name_uz = name_uz,
            name_en=name_en,
            name_ru=name_ru,
            slug=fake.slug(),
            category=Category.objects.get(id=fake.random_int(min=1, max=100)),
        ))
    Subcategory.objects.bulk_create(data)


def generate_orders() -> None:
    data = []
    fake = Faker()
    for _ in range(100):
        description = fake.text()
        description_ru = translate_en_ru(description)
        description_uz = translate_en_uz(description)
        description_en = description

        data.append(Order(
            user=BotUser.objects.get(id=fake.random_int(min=1, max=100)),
            category=Category.objects.get(id=fake.random_int(min=1, max=100)),
            subcategory=Subcategory.objects.get(id=fake.random_int(min=1, max=100)),
            description=description,
            description_uz = description_uz,
            description_en=description_en,
            description_ru=description_ru,
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
        
        body = fake.text()
        
        body_ru = translate_en_ru(body)
        body_uz = translate_en_uz(body)
        body_en = body
        data.append(Comment(
            user=BotUser.objects.get(id=fake.random_int(min=1, max=100)),
            body=body,
            body_uz = body_uz,
            body_en = body_en,
            body_ru = body_ru,
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
