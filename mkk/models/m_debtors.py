from django.db import models
from .m_department import department

# Create your models here.
class debtors(models.Model):
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
    total_amount = models.FloatField(verbose_name ='Итого',
                                     help_text="Считает автоматом",
                                     default = 0.0)
    
    
    
    def calculate(self):
        self.interest = self.loan_amount * 1.5
        self.total = self.loan_amount + self.interest
        if self.total > 20000:
            self.state_duty = ((self.total * 4) / 100) / 2
            self.state_duty = max(self.state_duty, 200)  
        else:
            self.state_duty = self.total - 20000
            self.state_duty = (self.state_duty * (3 * 100 + 800))
    
    
    def __str__(self):
        return self.name # TODO
