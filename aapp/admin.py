#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Derivatives, Serial
from .models import User
from .models import Cryptocurrency
from .models import NFT
from .models import Trade
from .models import Market
from .models import Earn
from .models import Finance
#from django.contrib.auth.models import Group

#admin.site.register(Venue, VenueAdmin)
admin.site.register(User)

# Remove Groups
#admin.site.unregister(Group)
admin.site.register(Serial)

#@admin.register(Serial)
#class Admin(admin.ModelAdmin):
#	list_display = ('name', 'address', 'phone')
#	ordering = ('name',)
#	search_fields = ('name', 'address')

admin.site.register(Cryptocurrency)
#@admin.register(Cryptocurrency)
#class CryptoAdmin(admin.ModelAdmin):
#	fields = (('name', 'serial'), 'event_date', 'description', 'manager', 'approved')
#	list_display = ('name', 'serial_date', 'serial')
#	list_filter = ('serial_date', 'venue')
#	ordering = ('serial_date',)


admin.site.register(NFT)
admin.site.register(Market)
admin.site.register(Derivatives)
admin.site.register(Trade)
admin.site.register(Earn)
admin.site.register(Finance)
