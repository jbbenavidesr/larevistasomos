import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'larevistasomos.settings')
django.setup()


from revista.models import Author 
from django.template.defaultfilters import slugify

authors = Author.objects.all()

for author in authors:
    slug = slugify(author.name)
    author.slug = slug
    author.save()