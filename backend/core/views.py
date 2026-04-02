import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import ChurchMember, ChurchEvent, Donation


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['churchmember_count'] = ChurchMember.objects.count()
    ctx['churchmember_regular'] = ChurchMember.objects.filter(membership_type='regular').count()
    ctx['churchmember_youth'] = ChurchMember.objects.filter(membership_type='youth').count()
    ctx['churchmember_senior'] = ChurchMember.objects.filter(membership_type='senior').count()
    ctx['churchevent_count'] = ChurchEvent.objects.count()
    ctx['churchevent_service'] = ChurchEvent.objects.filter(event_type='service').count()
    ctx['churchevent_bible_study'] = ChurchEvent.objects.filter(event_type='bible_study').count()
    ctx['churchevent_youth_group'] = ChurchEvent.objects.filter(event_type='youth_group').count()
    ctx['donation_count'] = Donation.objects.count()
    ctx['donation_tithe'] = Donation.objects.filter(donation_type='tithe').count()
    ctx['donation_offering'] = Donation.objects.filter(donation_type='offering').count()
    ctx['donation_building_fund'] = Donation.objects.filter(donation_type='building_fund').count()
    ctx['donation_total_amount'] = Donation.objects.aggregate(t=Sum('amount'))['t'] or 0
    ctx['recent'] = ChurchMember.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def churchmember_list(request):
    qs = ChurchMember.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(membership_type=status_filter)
    return render(request, 'churchmember_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def churchmember_create(request):
    if request.method == 'POST':
        obj = ChurchMember()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.membership_type = request.POST.get('membership_type', '')
        obj.join_date = request.POST.get('join_date') or None
        obj.status = request.POST.get('status', '')
        obj.ministry = request.POST.get('ministry', '')
        obj.address = request.POST.get('address', '')
        obj.save()
        return redirect('/churchmembers/')
    return render(request, 'churchmember_form.html', {'editing': False})


@login_required
def churchmember_edit(request, pk):
    obj = get_object_or_404(ChurchMember, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.membership_type = request.POST.get('membership_type', '')
        obj.join_date = request.POST.get('join_date') or None
        obj.status = request.POST.get('status', '')
        obj.ministry = request.POST.get('ministry', '')
        obj.address = request.POST.get('address', '')
        obj.save()
        return redirect('/churchmembers/')
    return render(request, 'churchmember_form.html', {'record': obj, 'editing': True})


@login_required
def churchmember_delete(request, pk):
    obj = get_object_or_404(ChurchMember, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/churchmembers/')


@login_required
def churchevent_list(request):
    qs = ChurchEvent.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(event_type=status_filter)
    return render(request, 'churchevent_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def churchevent_create(request):
    if request.method == 'POST':
        obj = ChurchEvent()
        obj.title = request.POST.get('title', '')
        obj.event_type = request.POST.get('event_type', '')
        obj.date = request.POST.get('date') or None
        obj.time = request.POST.get('time', '')
        obj.location = request.POST.get('location', '')
        obj.attendees = request.POST.get('attendees') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/churchevents/')
    return render(request, 'churchevent_form.html', {'editing': False})


@login_required
def churchevent_edit(request, pk):
    obj = get_object_or_404(ChurchEvent, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.event_type = request.POST.get('event_type', '')
        obj.date = request.POST.get('date') or None
        obj.time = request.POST.get('time', '')
        obj.location = request.POST.get('location', '')
        obj.attendees = request.POST.get('attendees') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/churchevents/')
    return render(request, 'churchevent_form.html', {'record': obj, 'editing': True})


@login_required
def churchevent_delete(request, pk):
    obj = get_object_or_404(ChurchEvent, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/churchevents/')


@login_required
def donation_list(request):
    qs = Donation.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(donor_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(donation_type=status_filter)
    return render(request, 'donation_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def donation_create(request):
    if request.method == 'POST':
        obj = Donation()
        obj.donor_name = request.POST.get('donor_name', '')
        obj.amount = request.POST.get('amount') or 0
        obj.donation_type = request.POST.get('donation_type', '')
        obj.date = request.POST.get('date') or None
        obj.method = request.POST.get('method', '')
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/donations/')
    return render(request, 'donation_form.html', {'editing': False})


@login_required
def donation_edit(request, pk):
    obj = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        obj.donor_name = request.POST.get('donor_name', '')
        obj.amount = request.POST.get('amount') or 0
        obj.donation_type = request.POST.get('donation_type', '')
        obj.date = request.POST.get('date') or None
        obj.method = request.POST.get('method', '')
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/donations/')
    return render(request, 'donation_form.html', {'record': obj, 'editing': True})


@login_required
def donation_delete(request, pk):
    obj = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/donations/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['churchmember_count'] = ChurchMember.objects.count()
    data['churchevent_count'] = ChurchEvent.objects.count()
    data['donation_count'] = Donation.objects.count()
    return JsonResponse(data)
