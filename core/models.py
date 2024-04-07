from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PaymentOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(PaymentOption, on_delete=models.CASCADE)
    account_details = models.CharField(max_length=255)

    def clean(self):
        option_name = self.option.name.lower()
        if option_name == 'mpesa':
            if not self.account_details.isdigit():
                raise ValidationError("Mpesa account details must be a 10-digit number.")
            elif len(self.account_details) != 10:
                raise ValidationError("Mpesa account details must be exactly 10 digits.")
        elif option_name == 'paypal' and not self.account_details.count('@') == 1:
            raise ValidationError("Paypal account details must be an email address.")
        elif option_name == 'airtm' and not '@' in self.account_details:
            raise ValidationError("Airtm account details must be an email address.")

    def __str__(self):
        return f"{self.option.name} - {self.account_details} - {self.user.username}"
