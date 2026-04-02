from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import ChurchMember, ChurchEvent, Donation
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusChurch with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexuschurch.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if ChurchMember.objects.count() == 0:
            for i in range(10):
                ChurchMember.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    membership_type=random.choice(["regular", "youth", "senior", "volunteer"]),
                    join_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["active", "inactive"]),
                    ministry=f"Sample {i+1}",
                    address=f"Sample address for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 ChurchMember records created'))

        if ChurchEvent.objects.count() == 0:
            for i in range(10):
                ChurchEvent.objects.create(
                    title=f"Sample ChurchEvent {i+1}",
                    event_type=random.choice(["service", "bible_study", "youth_group", "community", "special"]),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    time=f"Sample {i+1}",
                    location=f"Sample {i+1}",
                    attendees=random.randint(1, 100),
                    status=random.choice(["upcoming", "completed", "cancelled"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 ChurchEvent records created'))

        if Donation.objects.count() == 0:
            for i in range(10):
                Donation.objects.create(
                    donor_name=f"Sample Donation {i+1}",
                    amount=round(random.uniform(1000, 50000), 2),
                    donation_type=random.choice(["tithe", "offering", "building_fund", "mission", "special"]),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    method=random.choice(["cash", "card", "bank", "online"]),
                    status=random.choice(["received", "pledged"]),
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Donation records created'))
