from django.db import models
from django.utils.text import slugify
# Create your models here.
NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
]

class Subscribe(models.Model):
    first_name=models.CharField(max_length=100, help_text="Enter characters only")
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION)
    # option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION, default='M')


# def save(self, *args, **kwargs):
#         if not self.id:

#             self.slug = slugify(self.title)
#         #eturn self.save(*args, **kwargs)
#         return super(Subscribe, self).save(*args, **kwargs)
