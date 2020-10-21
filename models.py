from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class WorkOrService(models.Model):
    document = models.CharField('Документы', max_length=100)

    def __str__(self):
        return self.document

    class Meta:
        verbose_name = 'Услуга или работа'
        verbose_name_plural = 'Услуги или работы'


class Conditions(models.Model):
    condition = models.CharField('Условия', max_length=100)

    def __str__(self):
        return self.condition

    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'


class Documents(models.Model):
    name_of_the_organization = models.CharField('Название организации',
                                                max_length=100)
    address = models.CharField('Адрес', max_length=100)
    email = models.EmailField('Email', max_length=100)
    subject_of_a_contract = models.ForeignKey(WorkOrService,
                                              verbose_name='Предмет договора',
                                              on_delete=models.CASCADE)
    name_of_the_contract = models.CharField('Наименование договора',
                                            max_length=100)
    quantity = models.IntegerField('Количество')
    number_of_contract = models.TextField('Номер договора',
                                          max_length=100)
    date_of_signing = models.DateField()
    period_of_execution = models.DateField()
    price = models.IntegerField('Цена')
    share_of_payment = models.CharField('Доли платежа',
                                        max_length=100)
    term = models.DateField()
    other_conditions = models.ForeignKey(Conditions,
                                         verbose_name='Иные условия',
                                         on_delete=models.CASCADE)

    # загрузить текст

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Contract(models.Model):
    type = 'Договор Поставки'

    # Общая информация
    date_of_signing = models.DateField('Дата подписания')
    title = models.CharField('Наименование Организации', max_length=200)
    director = models.CharField('Генеральный директор', max_length=100)
    legal_address = models.CharField('Адрес', max_length=254)
    email = models.EmailField('E-mail', max_length=200)
    number_of_contract = models.CharField('Номер договора', max_length=250)

    # Условия Договора
    # Предмет логовора
    terms = models.TextField('Содержание договора', null=True)
    # Порядок исполнения

    # Предмет договора:
    # Открытие кнопка 'Выбрать' списка работы/услуги
    subject_of_a_contract = models.ForeignKey(WorkOrService,
                                              verbose_name='Предмет договора',
                                              on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=120)
    amount = models.CharField('Количество', max_length=100)

    # Загрузить текст
    file = models.FileField('Прикрепленный файл', blank=True, upload_to='static/upload')

    period_of_execution = models.DateField('Срок выполнения')

    # Automate
    date_of_creation = models.DateField('Дата создания', auto_now_add=True)

    PAYMENT = 'На этапе оплаты'
    SIGNING = 'На этапе подписывания'
    STATUS_CHOICES = [
        (PAYMENT, 'На этапе оплаты'),
        (SIGNING, 'На этапе подписывания')
    ]
    status = models.CharField(
        'Статус',
        max_length=21,
        choices=STATUS_CHOICES,
        default=SIGNING,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Timing(models.Model):
    DONE = 'Выполнено'
    NOT_DONE = 'Не выполнено'
    REACTION_CHOICES = [
        (DONE, 'Выполнено'),
        (NOT_DONE, 'Не выполнено')
    ]

    contract = models.ForeignKey(Contract, null=True, on_delete=models.SET_NULL)

    execution_period = models.DateField('Срок исполнения')
    subject = models.CharField('Количество товара', max_length=200)
    payment_period = models.DateField('Срок оплаты')
    amount = models.DecimalField('Сумма', max_digits=15, decimal_places=2, default=0.0)
    penalty = models.FloatField('Неустойка')
    reaction = models.CharField(
        'Реакция',
        max_length=12,
        choices=REACTION_CHOICES,
        default=NOT_DONE,
    )

    # claim = ('Претензия')
