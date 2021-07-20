from .models import *
from django.contrib import admin

# Register your models here.

admin.site.register(About)
admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Contact)


from django.contrib import admin
from jet.admin import CompactInline


class AboutInline(admin.TabularInline):
    model = About
    extra = 1
    show_change_link = True


class PortfolioInline(CompactInline):
    model = Portfolio
    extra = 1
    show_change_link = True


class StateAdmin(admin.ModelAdmin):
    inlines = (AboutInline, PortfolioInline)