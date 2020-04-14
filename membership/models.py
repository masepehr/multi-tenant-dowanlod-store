import datetime

from django.db import models

from stores.models import Store
from users.models import CustomerUser
from django.utils.translation import gettext_lazy as _


class MemberShipPlans(models.Model):
    MONTH1 =1
    MONTH3 = 3
    MONTH6 = 6
    YEARLY = 12

    TIME_RANGE_CHOICES = [

        (MONTH1, _('1 month')),
        (MONTH3, _('3 month')),
        (MONTH6, _('6 month')),
        (YEARLY, _('1 year')),
    ]

    type = models.IntegerField(choices=TIME_RANGE_CHOICES,default=MONTH1)
    price = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return "{}-{}month-{}$".format(self.store.name, self.type, self.price)


class MemberShipOrder(models.Model):
    PENDING = 'pending'
    CANCLED = 'canceled'
    UNSUCCESSFUL = 'unsuccessful'
    SUCCESSFUL = 'successful'

    ODRER_STATUS = [
        (PENDING, _('Waiting for paying')),
        (CANCLED, _('Cancled order')),
        (UNSUCCESSFUL, _('Unsuccessfull payment')),
        (SUCCESSFUL, _('Successful payment')),
    ]

    plan = models.ForeignKey(MemberShipPlans, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(choices=ODRER_STATUS,max_length=12, default=PENDING)
