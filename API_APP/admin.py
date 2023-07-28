from django.contrib import admin
from .models import * 

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'name',
        'roll',
        'city',
        'created_dt',
    ]


@admin.register(login)
class loginAdmin(admin.ModelAdmin):
    list_display= [
        'mobile',
        'profile_image',
        'verify_otp',
    ]

