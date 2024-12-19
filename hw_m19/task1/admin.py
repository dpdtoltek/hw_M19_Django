from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('username',)
    list_per_page = 30

    readonly_fields = ('balance',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('title',)
    search_fields = ('size', 'cost')
    list_per_page = 20
