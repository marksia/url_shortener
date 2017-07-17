import uuid
from django.db import models

# Create your models here.
class URLRedirect(models.Model):
    url = models.URLField(max_length=4096)
    unique_code = models.CharField(max_length=8, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None and self.unique_code in [None, '']:
            self.unique_code = self.uuid_generator()

        super(URLRedirect, self).save(*args, **kwargs)

    def uuid_generator(self):
        unique_code = uuid.uuid4().hex[:8].upper()
        if URLRedirect.objects.filter(unique_code=unique_code).exists():
            self.uuid_generator()
        else:
            return unique_code