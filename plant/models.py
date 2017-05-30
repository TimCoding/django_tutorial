from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.
class Type(models.Model):
    t_name = models.CharField(max_length=250)
    t_img = models.CharField(max_length=1000)
    t_description = models.CharField(max_length=1000)
    slug = models.SlugField(default='', blank=True)

    def save(self, *args, **kwargs):
        super(Type, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.t_name)
            self.save()

    def __str__(self):
        return self.t_name

    def get_absolute_url(self):
        return reverse("plant:detail", kwargs = {'slug': str(self.slug)})

class Plant(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200)
    p_img = models.CharField(max_length=200)
    p_description = models.CharField(max_length=1000)
    p_quantity = models.IntegerField()
    p_favorite = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True)

    def save(self, *args, **kwargs):
        super(Plant, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.p_name)
            self.save()

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        #Gacky solution to make the name of the type lower case
        return reverse("plant:plant", kwargs = {'type': str(self.type).lower(), 'pk': str(self.id), 'name': str(self.slug)})


