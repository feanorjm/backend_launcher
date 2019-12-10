from django.db import models
# Create your models here.


class background(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=150)
    imagen = models.FileField(upload_to='media/backgrounds', null=True, blank=True)
    activo = models.BooleanField(default=False, choices=((True,"Si"),(False,"No")))

    def __str__(self):
        return str(self.nombre)

class Title(models.Model):
    en = models.CharField(max_length=45)
    es = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id) + ' title'


class Description(models.Model):
    en = models.TextField(max_length=150)
    es = models.TextField(max_length=150)

    def __str__(self):
        return str(self.id) + ' descripción'

class Trailer(models.Model):
    en = models.CharField(max_length=45)
    es = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id) + ' trailer'

class Image(models.Model):
    image = models.FileField(upload_to='media/backgrounds', null=True, blank=True)

    def __str__(self):
        return str(self.image)


class App(models.Model):
    name = models.CharField(max_length=45)
    skip = models.BooleanField(default=False)
    start = models.DateTimeField()
    end = models.DateTimeField()
    rating = models.DecimalField
    year = models.CharField(max_length=4)
    package = models.CharField(max_length=45)
    uri = models.CharField(max_length=100)
    #app = models.ForeignKey(App, related_name='titles', on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, default=None)
    description = models.ForeignKey(Description, on_delete=models.CASCADE , default=None)
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE , default=None)
    banner = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    #images = models.ForeignKey(Image, on_delete=models.CASCADE , default=None)
    images = models.ManyToManyField(Image, default=None)


    def __str__(self):
        return str(self.name)




