from django.db import models

class Author(models.Model):
    name = models.CharField("Nombre", max_length=200, unique=True)
    school = models.CharField("Colegio", max_length=200)
    ig_link = models.URLField("Instagram Link", blank= True)
    ig_user = models.CharField("Instagram User", max_length=50, blank= True)
    photo = models.ImageField("Foto", upload_to='autores')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField("Nombre ", max_length=50, unique=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Article(models.Model):
    title = models.CharField("Titulo", max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete= models.CASCADE,
        related_name = 'articulos',
        verbose_name = "Autor"
    )
    body = models.TextField("Contenido")
    description = models.TextField("Descripción corta")
    pub_date = models.DateField("Fecha de publicación")
    update = models.DateTimeField("Última modificación", auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE,
        related_name = 'articulos',
        verbose_name = "Categoría"
    )
    status = models.IntegerField("Estado", choices=STATUS, default = 0)
    claps = models.IntegerField("Aplausos", default = 0)
    img1 = models.ImageField("Imagen principal", upload_to='articulos', blank=True)
    img2 = models.ImageField("Segunda imagen", upload_to='articulos', blank=True)

    class Meta:
        ordering = ['-update']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name = 'comments',
        verbose_name= 'Articulo'
    )
    name = models.CharField('Nombre', max_length = 80)
    body = models.TextField()
    created_on = models.DateTimeField('Creación', auto_now_add = True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return 'Comentario por {} en {}'.format(self.name, self.article)