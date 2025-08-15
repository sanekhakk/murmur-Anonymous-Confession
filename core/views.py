from django.shortcuts import render, redirect
from .models import Confession , Reply
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

def home(request):
    # Only show trending confessions on home page
    trending_confessions = Confession.objects.filter(
        Q(is_trending=True) | Q(upvotes__gt=10)
    ).order_by('-upvotes', '-created_at')
    return render(request, 'core/home.html', {
        'trending': trending_confessions,
    })

def recent_confessions(request):
    # Show all recent confessions on separate page
    recent_confessions = Confession.objects.all().order_by('-created_at')
    return render(request, 'core/recent_confessions.html', {
        'confessions': recent_confessions,
    })
    

def post_confession(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        mood = request.POST.get('mood')  # Get the selected mood
        if content:
            Confession.objects.create(message=content, mood=mood if mood else None )
    
    return render(request, 'core/post_confession.html', {})

def upvote_confession(request, confession_id):
    if request.method == "POST":
        confession = get_object_or_404(Confession, id=confession_id)
        confession.upvotes += 1
        confession.save()
        return JsonResponse({'upvotes': confession.upvotes})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_protect
def add_reply(request, confession_id):
    if request.method == "POST":
        confession = get_object_or_404(Confession, id=confession_id)
        reply_text = request.POST.get("reply_text")
        if reply_text:
            Reply.objects.create(confession=confession, text=reply_text)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def contact(request):
    """
    Display the contact page
    """
    return render(request, 'core/contact.html')