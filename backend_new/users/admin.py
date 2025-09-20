from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'user_type', 'is_staff', 'is_active', 'created_at')
    list_filter = ('role', 'user_type', 'is_staff', 'is_active', 'is_verified', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'business_name')
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'profile_picture')}),
        ('Address', {'fields': ('address', 'city', 'state', 'postal_code')}),
        ('Business Info', {'fields': ('business_name', 'business_type', 'is_verified')}),
        ('Roles', {'fields': ('role', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at', 'date_joined', 'last_login')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'user_type'),
        }),
    )
