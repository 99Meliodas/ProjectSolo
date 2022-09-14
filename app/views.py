from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth import authenticate
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('contact')
    else:
        form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})


def service(request):
    return render(request, 'service.html')

