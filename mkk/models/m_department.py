from django.db import models

# Create your models here.
class department(models.Model):
    name = models.CharField(verbose_name = 'Имя',
                            max_length=50,
                            help_text="Введи имя")
    letter = models.CharField(verbose_name = 'Буква отделения',
                              max_length=10,
                                help_text="Введи имя")