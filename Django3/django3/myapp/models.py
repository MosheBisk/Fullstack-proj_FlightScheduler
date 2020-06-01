from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class webDevedopment(models.Model):

    # DJANGO = 'Dj'
    # ANGULAR = 'NG'
    # REACT = 'RE'

    # FRAMEWORKS = [
    #     (DJANGO, 'Django'),
    #     (ANGULAR, 'Angular'),
    #     (REACT, 'React'),
    # ]

    class Language(models.TextChoices):
        DJANGO = 'Dj', _('Django')
        ANGULAR = 'NG', _('Angular')
        REACT = 'RE', _('React')
 
    frameworks = models.CharField(
        max_length=2,
        choices = Language.choices, #FRAMEWORKS,
        default = Language.DJANGO,
    )

class Size(models.IntegerChoices):
    XS = 0, _('X-Small')
    S = 1, _('Small')
    M = 2, _('Medium')
    L = 3, _('Large')
