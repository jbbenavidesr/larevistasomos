from django.db import models

from revista.models import Author

class Gallery(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete= models.CASCADE,
        related_name = 'fotos',
        verbose_name = "Autor"
    )

    
    image = models.ImageField("Foto", upload_to='Gallery/')
