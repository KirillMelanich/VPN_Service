from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import  FormView

from .forms import RegisterForm, SiteForm, SiteSearchForm, ProfileForm
from .models import User, Site, Profile


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
    template_name = 'vpn/site_list.html'
    context_object_name = 'site_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SiteListView, self).get_context_data(**kwargs)

        site_name = self.request.GET.get("site_name", "")

        context["search_form"] = SiteSearchForm(
            initial={
                "site_name": site_name
            }
        )

        return context

    def get_queryset(self):
        queryset = Site.objects.filter(user=self.request.user)
        form = SiteSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                site_name__icontains=form.cleaned_data["site_name"],
            )

        return queryset


class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Site
    form_class = SiteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SiteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Site


class SiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Site
    form_class = SiteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Site
    success_url = reverse_lazy("vpn:site-list")
    template_name = "vpn/site_confirm_delete.html"

    def get_queryset(self):
        return Site.objects.filter(user=self.request.user)


# class UserDetailView(LoginRequiredMixin, generic.DetailView):
#     model = User
#     queryset = User.objects.all()


# @login_required
# def profile_view(request):
#     return render(request, "vpn/profile.html")

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'vpn/profile.html'


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("vpn:profile-detail")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
