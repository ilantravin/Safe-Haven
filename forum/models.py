from django.db import models



# parent model
class forum(models.Model):
    name = models.CharField(max_length=200, default="אנונימי", verbose_name="שם")
    email = models.EmailField(max_length=200, null=True, verbose_name="אימייל")  # only email allowed
    topic = models.CharField(max_length=300, verbose_name="נושא")
    description = models.TextField(default=None, blank=True, verbose_name="תיאור")
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="תאריך")

    def __str__(self):
        return str(self.topic)
    class Meta:
        verbose_name_plural = "בקשות תרומה"


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE, default=None, verbose_name="הנושא עליו תרצה להגיב")
    discuss = models.TextField(max_length=5000, default=None, blank=True, verbose_name="התגובה")
    name = models.CharField(max_length=100, blank=True, default=None, verbose_name="שם")

    def __str__(self):
        return str(self.forum)
    class Meta:
        verbose_name_plural = "תגובות לבקשות תרומה"