from django.db import models

class ChurchMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    membership_type = models.CharField(max_length=50, choices=[("regular", "Regular"), ("youth", "Youth"), ("senior", "Senior"), ("volunteer", "Volunteer")], default="regular")
    join_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], default="active")
    ministry = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class ChurchEvent(models.Model):
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=[("service", "Service"), ("bible_study", "Bible Study"), ("youth_group", "Youth Group"), ("community", "Community"), ("special", "Special")], default="service")
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=255, blank=True, default="")
    location = models.CharField(max_length=255, blank=True, default="")
    attendees = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("upcoming", "Upcoming"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="upcoming")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Donation(models.Model):
    donor_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    donation_type = models.CharField(max_length=50, choices=[("tithe", "Tithe"), ("offering", "Offering"), ("building_fund", "Building Fund"), ("mission", "Mission"), ("special", "Special")], default="tithe")
    date = models.DateField(null=True, blank=True)
    method = models.CharField(max_length=50, choices=[("cash", "Cash"), ("card", "Card"), ("bank", "Bank"), ("online", "Online")], default="cash")
    status = models.CharField(max_length=50, choices=[("received", "Received"), ("pledged", "Pledged")], default="received")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.donor_name
