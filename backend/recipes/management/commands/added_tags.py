from django.core.management import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    help = 'Создание шаблонных тегов в базе данных.'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Первое', 'color': '#B840CF', 'slug': 'first'},
            {'name': 'Второе', 'color': '#003153', 'slug': 'second'},
            {'name': 'Десерт', 'color': '#FF6347', 'slug': 'dessert'},
            {'name': 'Завтрак', 'color': '#3DD25A', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#10B7FF', 'slug': 'lunch'},
            {'name': 'Ужин', 'color': '#C71585', 'slug': 'dinner'},
            {'name': 'Восточная кухня', 'color': '#D8FF10', 'slug': 'eastern'},
            {'name': 'Русская кухня', 'color': '#8B0000', 'slug': 'russian'},

        ]
        try:
            Tag.objects.bulk_create(Tag(**tag) for tag in data)
        except ValueError:
            print('Неопределенное значение.')
        except Exception:
            print('Что-то пошло не так!')
        else:
            print('Создание тегов окончено.')
