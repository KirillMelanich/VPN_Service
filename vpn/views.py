from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, FormView

from .forms import RegisterForm
from .models import User, Site


@login_required
def index(request):
    """View function for the home page of the site."""

    num_users = User.objects.count()
    num_sites = Site.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_sites": num_sites,
        "num_visits": num_visits + 1,
    }

    return render(request, "vpn/index.html", context=context)


class SiteListView(LoginRequiredMixin, generic.ListView):
    model = Site
    paginate_by = 5
    queryset = Site.objects.all()


class SiteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Site


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    queryset = User.objects.all()


@login_required
def profile_view(request):
    return render(request, "vpn/profile.html")


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("vpn:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

