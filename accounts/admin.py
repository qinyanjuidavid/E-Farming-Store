from django.contrib import admin
from accounts.models import User
from accounts.forms import UserChangeForm,UserCreationForm

class Myadmin(admin.ModelAdmin):
    search_fields=['email','username']
    form=UserChangeForm
    add_form=UserCreationForm
    list_display=('username','first_name','last_name','email','is_admin','is_staff','is_active')
    list_filter=('is_admin','is_staff','is_active')

admin.site.register(User,Myadmin)
