from django.db import models
from datetime import date


# create a new model for report app

class report(models.Model):
    date = models.DateField(default=date.today, verbose_name="תאריך ")  # date of the report
    name = models.CharField(max_length=100, verbose_name="שם המדווח ")  # name of the reporter
    text = models.TextField(blank=True, verbose_name="תוכן הדיווח ")  # the content of the report

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "דיווחים"