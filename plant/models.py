from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Type(models.Model):
    t_name = models.CharField(max_length=250)
    t_img = models.CharField(max_length=1000)
    t_description = models.CharField(max_length=1000)
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        super(Type, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.t_name) + "-" + str(self.id)
            self.save()

    def __str__(self):
        return self.t_name

class Plant(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200)
    p_img = models.CharField(max_length=200)
    p_description = models.CharField(max_length=1000)
    p_quantity = models.IntegerField()
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        super(Plant, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.p_name) + "-" + str(self.id)
            self.save()

