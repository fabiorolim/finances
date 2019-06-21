from django.db import models


class Account(models.Model):
    TYPE_ACCOUNTS = (
        ('receber', 'receber'),
        ('pagar', 'pagar'),
    )
    TYPE_PAYMENTS = (
        ('dinheiro', 'dinheiro'),
        ('cartão', 'cartão'),
        ('transferência', 'transferência'),
    )
    data_add = models.DateTimeField(auto_now_add=True)
    account_data = models.DateField(null=False, verbose_name='Data')
    description = models.TextField(null=False, verbose_name='Descrição')
    value = models.DecimalField(decimal_places=0, null=False, max_digits=10,
                                verbose_name='Valor')
    type = models.CharField(null=False, choices=TYPE_ACCOUNTS, max_length=7,
                            verbose_name='Tipo')
    type_payment = models.CharField(null=False, choices=TYPE_PAYMENTS,
                                    max_length=13,
                                    verbose_name='Meio de pagamento')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='Categoria')

    def __str__(self):
        return f'{self.description} em: {self.account_data}'

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Category(models.Model):
    data_add = models.DateField(auto_now_add=True)
    desciption = models.TextField(null=True, verbose_name='Descrição')

    def __str__(self):
        return self.desciption

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
