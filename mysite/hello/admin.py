from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.
class PassengerInline(admin.StackedInline):
    # relaciona a tabela passenger com a flights o trough indica a tabela de relacionamento delas pelo many2many
    model = Passenger.flights.through
    #consigo adicionar um passageiro por vez
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
