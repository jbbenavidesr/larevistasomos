from django.db import models

from revista.models import Author, image_filename, STATUS

class Gallery(models.Model):
    title = models.CharField("Titulo", max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete= models.CASCADE,
        related_name = 'fotos',
        verbose_name = "Autor"
    )
    description = models.TextField("Descripción", blank=True)

    def path(self, filename):
        return 'gallery/' + image_filename(self.title , filename)
    image = models.ImageField("Foto", upload_to=path)

    status = models.IntegerField("Estado", choices=STATUS, default = 1)
