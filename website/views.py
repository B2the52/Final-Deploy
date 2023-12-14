from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView
from website.models import Service, Review, RequestService
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.

def index(request):
    num_services = Service.objects.all().count()
    reviews = Review.objects.all().order_by('-review_id')[:5]  # Limiting to 5 reviews for example

    context = {
        'num_services': num_services,
        'reviews': reviews,  # Include reviews in the context
    }
    return render(request, 'index.html', context=context)


def about_us(request):
    num_services = Service.objects.all().count()
    context = {
        'num_services': num_services
    }
    return render(request, 'about_us.html', context=context)


def blog(request):
    num_services = Service.objects.all().count()
    context = {
        'num_services': num_services
    }
    return render(request, 'blog.html', context=context)


class ServiceListView(generic.ListView):
    model = Service


class ServiceDetailView(generic.DetailView):
    model = Service


class ServiceCreate(CreateView):
    model = Service
    fields = ['service_id', 'service_title', 'service_info', 'service_cost', 'service_img']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('service_list'))


class ReviewCreate(CreateView):
    model = Review
    fields = ['review_rating', 'review_comments', 'service_id']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('index'))


class RequestServiceCreate(CreateView):
    model = RequestService
    fields = ['contact_id']
