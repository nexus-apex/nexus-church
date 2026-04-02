from django.contrib import admin
from .models import ChurchMember, ChurchEvent, Donation

@admin.register(ChurchMember)
class ChurchMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "membership_type", "join_date", "created_at"]
    list_filter = ["membership_type", "status"]
    search_fields = ["name", "email", "phone"]

@admin.register(ChurchEvent)
class ChurchEventAdmin(admin.ModelAdmin):
    list_display = ["title", "event_type", "date", "time", "location", "created_at"]
    list_filter = ["event_type", "status"]
    search_fields = ["title", "time", "location"]

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ["donor_name", "amount", "donation_type", "date", "method", "created_at"]
    list_filter = ["donation_type", "method", "status"]
    search_fields = ["donor_name"]
