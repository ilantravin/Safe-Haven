from django.db import models


# Create your models here.
class AidOrg(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="")
    description = models.TextField()
    website = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'

    class Meta:
        verbose_name_plural = "ארגוני סיוע"
