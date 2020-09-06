from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

import markdown


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url = image.image.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html

def image_filename(name, filename):
    fname, dot, extension = filename.rpartition('.')
    slug = slugify(name)
    return '%s.%s' % (slug, extension) 

class Author(models.Model):
    name = models.CharField("Nombre", max_length=200, unique=True)
    school = models.CharField("Colegio", max_length=200, blank=True)
    ig_user = models.CharField("Instagram User (no @)", max_length=50, blank= True)
    slug = models.SlugField("slug")

    def path(self, filename):
        return 'autores/' + image_filename(self.name , filename)

    photo = models.ImageField("Foto", upload_to= path, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

    def ig_url (self):
        return 'https://www.instagram.com/%s/' % self.ig_user
    
    

class Category(models.Model):
    name = models.CharField("Nombre ", max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Issue(models.Model):

    number = models.IntegerField("Número", primary_key=True)
    pub_date = models.DateField("Fecha de publicación")
    current = models.BooleanField("Edición actual", default=False)

    def __str__(self):
        return f"Edición {self.number}"

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Edición'
        verbose_name_plural = 'Ediciones'

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
    bib = models.TextField("Bibliografía", blank=True)
    description = models.TextField("Descripción corta", blank=True)
    pub_date = models.DateField("Fecha de publicación")
    update = models.DateTimeField("Última modificación", auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE,
        related_name = 'articles',
        verbose_name = "Categoría"
    )
    status = models.IntegerField("Estado", choices=STATUS, default = 1)
    template_name = models.CharField('Layout del articulo', max_length=50 ,default='article.html')
    issue = models.ForeignKey(
        Issue, 
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="Edición",
        null=True
    )


    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.title

    def body_html( self ):
        return markdown_to_html( self.body, self.images.all() )
    
    def get_first_image(self):
        if self.images.all():
            return self.images.all()[0]
        else:
            return None

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name = 'images',
        verbose_name= 'Articulo'
    )

    def path(self, filename):
        return self.article.category.slug + '/' + image_filename(self.article.title+'-' + self.name, filename) 

    image = models.ImageField(upload_to= path)
    source = models.URLField('Fuente', blank = True)
    update = models.DateTimeField('Última modificación', auto_now=True)

    def __str__( self ):
        return self.name

    class Meta:
        ordering = ['-update']
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'


class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name = 'comments',
        verbose_name= 'Articulo'
    )
    name = models.CharField('Nombre', max_length = 80)
    body = models.TextField('Contenido')
    email = models.EmailField(max_length=254)
    created_on = models.DateTimeField('Creación', auto_now_add = True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return 'Comentario por {} en {}'.format(self.name, self.article)
