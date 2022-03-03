from django.contrib import admin

from rphusers.models import AddSocials, Socials, UserProfile

admin.site.register(UserProfile)
admin.site.register(Socials)
admin.site.register(AddSocials)
