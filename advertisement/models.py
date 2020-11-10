from django.db import models
from django.template.defaultfilters import slugify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


def image_filename(name, filename):
    fname, dot, extension = filename.rpartition('.')
    slug = slugify(name)
    return '%s.%s' % (slug, extension)


class Advertisement(models.Model):

    name = models.CharField("Emprendimiento", max_length=100)
    position = models.IntegerField("Posición")
    url = models.URLField("Link", max_length=200)
    status = models.IntegerField("Estado", choices=STATUS, default=0)

    def path(self, filename):
        return f'ads/{image_filename(self.name, filename)}'

    def m_path(self, filename):
        return f'ads/m_{image_filename(self.name, filename)}'

    image = models.ImageField("Image", upload_to=path)
    image_mobile = models.ImageField(
        "Image - Mobile", upload_to=m_path, blank=True)

    class Meta:
        verbose_name = "Pauta"
        verbose_name_plural = "Pautas"

    def __str__(self):
        return self.name
