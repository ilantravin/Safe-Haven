from django.db import models


class Donations(models.Model):
    """Donations model"""
    name = models.CharField(max_length=100, verbose_name="שם")
    id_number = models.CharField(max_length=100, verbose_name="תעודת זהות")
    credit_number = models.CharField(max_length=100, blank=True, verbose_name="מספר אשראי")
    cvc = models.CharField(max_length=100, blank=True, verbose_name="3 ספרות מאחורי הכרטיס")
    amount = models.CharField(max_length=100, verbose_name="סכום")

    def __str__(self):
        return f"{self.name} - {self.amount}₪"
    
    class Meta:
        verbose_name_plural = "תרומות"