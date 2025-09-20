from django.contrib import admin
from .models import Company, Contact, Product, Tax, ChartOfAccounts

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'created_at')
    list_filter = ('city', 'state', 'created_at')
    search_fields = ('name', 'email', 'tax_id')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_type', 'email', 'phone', 'company', 'is_active')
    list_filter = ('contact_type', 'is_active', 'company', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'product_type', 'unit_price', 'company', 'is_active')
    list_filter = ('product_type', 'is_active', 'company', 'created_at')
    search_fields = ('name', 'sku', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'tax_type', 'company', 'is_active')
    list_filter = ('tax_type', 'is_active', 'company', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ChartOfAccounts)
class ChartOfAccountsAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type', 'company', 'is_active')
    list_filter = ('account_type', 'is_active', 'company', 'created_at')
    search_fields = ('code', 'name')
    readonly_fields = ('created_at', 'updated_at')