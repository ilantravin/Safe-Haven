from django.db import models
from django.contrib.auth.models import User
from datetime import date

# create a new model for report app

class hostReq(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=100, verbose_name="שם ושם משפחה ")
    street = models.CharField(max_length=100, default='', verbose_name="רחוב ")
    city = models.CharField(max_length=100, verbose_name="עיר ")
    housetype = models.CharField(max_length=15, verbose_name="סוג הנכס ")
    rooms = models.IntegerField(verbose_name="מספר חדרים ")
    beds = models.IntegerField(verbose_name="מספר מיטות ")
    kosher = models.BooleanField(verbose_name="כשרות ")
    phone = models.CharField(max_length=10, verbose_name="טלפון ")
    email = models.EmailField(max_length=100, verbose_name="אימייל ")
    description = models.TextField(blank=True, verbose_name="תיאור הנכס ")
    thumb = models.ImageField(upload_to='media/', blank=True, verbose_name="תמונה של הנכס ")
    is_occupied = models.BooleanField(default=False, verbose_name="האם הנכס תפוס")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_kosher_status(self):
        return 'כן' if self.kosher else 'לא'


    def __str__(self):
        return self.fullname


    class Meta:
        verbose_name_plural = "בקשות אירוח"