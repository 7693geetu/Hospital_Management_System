
from django.contrib import admin
from .models import Login

# Current import causing the error
from .models import Login

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username','password')


'''from .models import LoginRecord
from django.contrib import admin
from .models import DemoSession
from .models import Doctor



@admin.register(DemoSession)
class DemoSessionForm(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'preferred_day', 'preferred_time')

@admin.register(LoginRecord)
class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'get_description')

    def get_description(self, obj):
        return f"{obj.name} is a {obj.specialization}.'''