from django.db import models


class NewAccounts(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=4)
    phoneNum = models.TextField()
    maile = models.TextField()
    national_id = models.TextField()
    balanc = models.IntegerField(default=0)
    account_type = models.CharField(max_length=10)


# Creadit card form database
class creditcards(models.Model):
    fullname = models.CharField(max_length=100)
    phoneNum = models.TextField()
    maile = models.TextField()
    monthluSalary = models.IntegerField(default=0)
    type = models.CharField(max_length=20, null=True)
    Age = models.IntegerField()


# fedback messages database
class Feedback(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    subjet = models.CharField(max_length=100,null=True)
    message = models.TextField()
    maile = models.TextField()
