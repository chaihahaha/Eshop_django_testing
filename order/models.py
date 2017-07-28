from django.db import models
# Create your models here.


class Ptype(models.Model):
    name = models.CharField('type', max_length=10)

    def __str__(self):
        return "分类:%s" % self.name


class Product(models.Model):
    name = models.CharField("product name", max_length=30)
    price = models.FloatField('price', default=10)
    ptype = models.ForeignKey(Ptype)
    texts = models.TextField('article', max_length=5000)
    img = models.ImageField('img', upload_to="product", max_length=100)
    music = models.FileField('music', upload_to="product", max_length=100)
    video = models.FileField('video', upload_to="product", max_length=100)

    def __str__(self):
        return "名称:%s 价格:%f " % (self.name, self.price)
