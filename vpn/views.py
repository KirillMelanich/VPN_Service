from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import User, Site, InternalRoute


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

    return render(request, "taxi/index.html", context=context)


class SiteListView(LoginRequiredMixin, generic.ListView):
    model = Site
    paginate_by = 5
    queryset = Site.objects.all()


class SiteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Site


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    queryset = User.objects.all()

