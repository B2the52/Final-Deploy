from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView
from website.models import Service, Review, ServiceRequest, Invoice, BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin
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


class InvoiceCreate(CreateView):
    model = Invoice
    fields = ['invoice_no', 'invoice_date', 'invoice_total', 'invoice_description', 'service_id']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('index'))


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'blog_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(reverse('index'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


def blog(request):
    # Update this view to pass blog posts to the template
    num_services = Service.objects.all().count()
    blog_posts = BlogPost.objects.all().order_by('-publish_date')
    context = {
        'num_services': num_services,
        'blog_posts': blog_posts,
    }
    return render(request, 'blog.html', context=context)
