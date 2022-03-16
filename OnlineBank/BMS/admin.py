from django.contrib import admin
from .models import NewAccounts
from .models import creditcards
from .models import Feedback

admin.site.register(NewAccounts)
admin.site.register(creditcards)
admin.site.register(Feedback)
# Register your models here.
