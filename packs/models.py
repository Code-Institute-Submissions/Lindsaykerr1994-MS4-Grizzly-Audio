from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Pack(models.Model):
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    publish_date = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    reduced_price = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sales = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=False, blank=False,
                              default='../../media/noimage.png')

    def __str__(self):
        return self.name
