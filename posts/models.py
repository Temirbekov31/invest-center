from django.db import models
from tinymce import models as tinymce_models

class Post(models.Model):
    titles = models.CharField(max_length=100)
    texts = tinymce_models.HTMLField()
    def __str__(self):
        return self.titles
