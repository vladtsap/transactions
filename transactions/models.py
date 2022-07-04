from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    telegram_id = models.BigIntegerField()
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    bank_clients = models.ManyToManyField('BankClient')
    bank_accounts = models.ManyToManyField('BankAccount')
    bank_jars = models.ManyToManyField('BankJar')


class BankClient(models.Model):
    id = models.UUIDField(primary_key=True)
    external_id = models.CharField(max_length=60)
    name = models.CharField(max_length=100)
    webhook_url = models.CharField(max_length=200)
    permissions = models.CharField(max_length=20)


class BankAccount(models.Model):
    id = models.UUIDField(primary_key=True)
    external_id = models.CharField(max_length=60)
    send_id = models.CharField(max_length=60)
    balance = models.BigIntegerField()
    credit_limit = models.BigIntegerField()
    type = models.CharField(max_length=20)
    currency_code = models.IntegerField()
    cashback_type = models.CharField(max_length=20)
    masked_pan = models.JSONField()
    iban = models.CharField(max_length=40)
    client_id = models.ForeignKey(BankClient, on_delete=models.CASCADE)


class BankJar(models.Model):
    id = models.UUIDField(primary_key=True)
    external_id = models.CharField(max_length=60)
    send_id = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    currency_code = models.IntegerField()
    balance = models.BigIntegerField()
    goal = models.BigIntegerField()
    client_id = models.ForeignKey(BankClient, on_delete=models.CASCADE)


class BankTransaction(models.Model):
    id = models.UUIDField(primary_key=True)
    external_id = models.CharField(max_length=100)
    time = models.BigIntegerField()
    description = models.CharField(max_length=200)
    mcc = models.IntegerField()
    original_mcc = models.IntegerField()
    hold = models.BooleanField()
    amount = models.BigIntegerField()
    operational_amount = models.BigIntegerField()
    currency_code = models.IntegerField()
    commission_rate = models.BigIntegerField()
    cashback_amount = models.BigIntegerField()
    balance = models.BigIntegerField()
    comment = models.CharField(max_length=200, null=True, blank=True)
    receipt_id = models.CharField(max_length=60, null=True, blank=True)
    invoice_id = models.CharField(max_length=60, null=True, blank=True)
    counter_edrpou = models.CharField(max_length=60, null=True, blank=True)
    counter_iban = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(BankClient, on_delete=models.CASCADE)
    account_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)
    jar_id = models.ForeignKey(BankJar, on_delete=models.CASCADE, null=True, blank=True)
