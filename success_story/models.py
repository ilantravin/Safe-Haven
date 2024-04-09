from django.db import models
from datetime import date


class story(models.Model):
    date = models.DateField(default=date.today, verbose_name='תאריך')
    name = models.CharField(max_length=100, blank=False, verbose_name='שם')
    text = models.TextField(max_length=5000, blank=False, verbose_name='תיאור')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "סיפורי הצלחה"

