from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class summer_note(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField()
