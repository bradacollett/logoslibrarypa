from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
   add_form = CustomUserCreationForm
   form = CustomUserChangeForm
   model = CustomUser
   list_display = ['email', 'username', 'first_name', 'last_name', 'date_of_birth', 'address1', 'address2', 'city',
                  'state','zip','phone','type',]


admin.site.register(CustomUser, CustomUserAdmin)