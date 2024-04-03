from django.db import models
from .m_department import department

# Create your models here.
class m_debtors(models.Model):
    department = models.ForeignKey("department",
                                   null=True,
                                   on_delete=models.PROTECT,
                                   verbose_name = 'Подразделение')
    surname = models.CharField(verbose_name = 'Фамилия',
                               max_length=30,
                               help_text="Введи фамилию")
    name = models.CharField(verbose_name = 'Имя',
                            max_length=30,
                            help_text="Введи имя")
    lastname = models.CharField(verbose_name = 'Отчество',
                                max_length=30,
                                help_text="Введи отчество")
    date_birth = models.DateField(verbose_name = 'Дата рождения',
                                  help_text="Введи дату рождения")
    place_birth = models.TextField(verbose_name = 'Место рождения',
                                   help_text="Введи место рождения")
    contract_number = models.TextField(verbose_name = 'Номер договора',
                                       help_text="Введи номер договора")
    agreement_date = models.DateField(verbose_name = 'Дата договора',
                                      help_text="Введи дату договора")
    loan_amount = models.FloatField(verbose_name = 'Сумма займа',
                                    help_text="Введи сумму займа")

    interest = models.FloatField(verbose_name ='Процент',
                                 help_text="Считает автоматом",
                                 default = 0.0)
    state_duty = models.FloatField(verbose_name ='Пошлина',
                                   help_text="Считает автоматом",
                                   default = 0.0)
    total = models.FloatField(verbose_name ='Итого',
                                     help_text="Считает автоматом",
                                     default = 0.0)
    
    def save(self, *args, **kwargs):
        # Расчет процентов
        self.interest = self.loan_amount * 1.5  # Сумма займа * 1.5, как вы описали

        # Расчет итого
        self.total = self.loan_amount + self.interest  # Сумма займа + Проценты

        # Расчет пошлины
        if self.total < 20000:
            duty_temp = ((self.total * 4) / 100) / 2
            self.state_duty = max(duty_temp, 200)  # Округление по формуле

        else:
            temp_total = self.total - 20000
            duty_temp = ((temp_total * 3) / 100 + 800) / 2
            self.state_duty = duty_temp

        super(m_debtors, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = u'Должник'
        verbose_name_plural = u'Должники'
