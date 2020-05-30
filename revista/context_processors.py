from revista.models import Category
import datetime

def get_current_year(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_year': current_datetime.year
    }


def navbar(request):
    kwargs = {
        'categories': Category.objects.all(),
        'contact': {
            'name': 'Contáctenos', 
            'link': 'contact:contact'
        },
        'about_us': {
            'name': '¿Quienes SOMOS?', 
            'link': 'revista:about_us'
        },
        'home': {
            'name': 'Inicio', 
            'link': 'revista:home'
        },
        'authors': {
            'name': 'Autores', 
            'link': 'revista:authors'
        },
        'archive': {
            'name': 'Archivo', 
            'link': 'revista:archive_index'
        }
    }
    return kwargs
    