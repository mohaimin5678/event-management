from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import CategoryForm, EventForm, ParticipantForm, EventUpdateForm, ParticipantUpdateForm, CategoryUpdateForm
from events.models import Event,Participant,Category
from django.db.models import Q
from django.urls import reverse
from django.utils.timezone import now
# Create your views here.

def home(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.select_related('category').filter( Q(name__icontains=query) | Q(location__icontains=query))
    else:
        events = Event.objects.select_related('category').all()
    return render(request, "index.html", {'events':events})

def dashboard_page(request):
    return render(request, "dashboard.html")

def event_search_view(request):
    query = request.GET.get('q')
    events = []
    if query:
        events = Event.objects.filter(Q(name__icontains=query))

    return render(request, 'event_search_from_dashboard.html', {'events': events})

def update_event(request, id):
    event = Event.objects.get(id=id)
    categories = Category.objects.all()
    success = False
    if request.method == 'POST':
        form = EventUpdateForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            success = True
            return redirect(f"{reverse('update_event', args=[id])}?success=1") 
    else:
        form = EventUpdateForm(instance=event)
    
    success = request.GET.get('success') == '1'
    context = {'form': form, 
               'event': event,
               'categories': categories,
               'success': success}
    return render(request, 'update_event.html', context)


def event_details(request, id):
    event = Event.objects.select_related('category').prefetch_related('participants').get(id=id)
    participants = event.participants.all()
    return render(request, "event_details.html", {'event': event, 'participants':participants})

def show_category(request):
    categories = Category.objects.all()
    return render(request, 'arrange_event.html', {'categories': categories})

def arrange_event_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('arrange_event')}?success=1")
    else:
        form = EventForm()
    success = request.GET.get('success') == '1'
    context = {
        'form': form,
        'categories': categories,
        'success': success
    }
    return render(request, 'arrange_event.html', context)

def delete_event_search_view(request):
    query = request.GET.get('q')
    events = []
    if query:
        events = Event.objects.filter(name__icontains=query)

    deleted = request.GET.get('deleted') == '1'
    context = {
        'events': events,
        'query': query,
        'deleted': deleted
    }
    return render(request, 'delete_event_search.html', context)

def delete_event_view(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect(f"{reverse('delete_event_search')}?deleted=1")

def insert_participant_view(request):
    events = Event.objects.all()
    form = ParticipantForm()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.save()
            form.save_m2m()
            return redirect(f"{reverse('insert_participant')}?success=1")
    else:
        form = ParticipantForm()
    
    success = request.GET.get('success') == '1'
    context ={
        'form': form, 
        'events': events,
        'success': success
    }
    return render(request, 'insert_participant.html',context)

def search_participant_view(request):
    query = request.GET.get('name')
    participants = []

    if query:
        participants = Participant.objects.filter(name__icontains=query)

    context={
        'participants': participants,
        'query': query,
    }
    return render(request, 'participant_search.html',context)

def update_participant_view(request, id):
    participant = Participant.objects.get(id=id)

    if request.method == 'POST':
        form = ParticipantUpdateForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('update_participant', args=[id])}?success=1")
    else:
        form = ParticipantUpdateForm(instance=participant)

    success = request.GET.get('success') == '1'

    return render(request, 'update_participant.html', {
        'form': form,
        'participant': participant,
        'success': success
    })

def search_participant_delete_view(request):
    query = request.GET.get('name')
    participants = []

    if query:
        participants = Participant.objects.filter(name__icontains=query)

    deleted = request.GET.get('deleted') == '1'
    context = {
        'participants': participants,
        'query': query,
        'deleted': deleted,
    }
    return render(request, 'participant_delete.html', context)

def delete_participant_view(request, id):
    participant = Participant.objects.get(id=id)
    participant.delete()
    return redirect(f"{reverse('search_participant_delete')}?deleted=1")


def category_create_view(request):
    return render(request, 'category_create.html')

def create_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('create_category')}?success=1")
    else:
        form = CategoryForm()
    success = request.GET.get('success') == '1'
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'category_create.html', context)



def category_update_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_update_list.html', {'categories': categories})

def update_category_view(request, id):
    category = Category.objects.get(id=id)
    
    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('update_category', args=[id])}?success=1")
    else:
        form = CategoryUpdateForm(instance=category)

    success = request.GET.get('success') == '1'
    context = {
        'form': form,
        'category': category,
        'success': success
    }
    return render(request, 'update_category.html', context)

def show_categories_to_delete(request):
    categories = Category.objects.all()
    deleted = request.GET.get('deleted') == '1'
    context = {
        'categories': categories,
        'deleted': deleted
    }
    return render(request, 'category_delete.html', context)


def delete_category_view(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(f"{reverse('delete_category_list')}?deleted=1")



def organizer_view(request):
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()

    today = now().date()
    upcoming_events = Event.objects.filter(event_date__gt=today).count()
    past_events = Event.objects.filter(event_date__lt=today).count()
    todays_events = Event.objects.filter(event_date=today)

    show = request.GET.get('show')
    if show == 'all':
        event_heading = "All Events"
        events = Event.objects.all()
    elif show == 'upcoming':
        event_heading = "Upcoming Events"
        events = Event.objects.filter(event_date__gt=today)
    elif show == 'past':
        event_heading = "Past Events"
        events = Event.objects.filter(event_date__lt=today)
    elif show == 'today':
        event_heading = "Today's Events"
        events = Event.objects.filter(event_date=today)
    else:
        event_heading = "Today's Events"
        events = Event.objects.filter(event_date=today)
    
    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'todays_events': todays_events,
        'event_heading': event_heading,
        'events': events,
    }

    return render(request, 'organizer.html', context)
