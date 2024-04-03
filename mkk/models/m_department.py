from django.db import models

# Create your models here.
class department(models.Model):
    name = models.CharField(verbose_name = 'Имя',
                            max_length=50,
                            null=True,
                            help_text="Введи имя")
    letter = models.CharField(verbose_name = 'Буква отделения',
                              max_length=10,
                                help_text="Введи имя")
    



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Подразделение'
        verbose_name_plural = u'Подразделения'