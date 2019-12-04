from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Profile
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from blog.forms import RegisterForm, ProfileForm
from django.shortcuts import render
from django.contrib import messages



class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class BlogCinemaView(TemplateView):
    model = Post
    template_name = 'cinema.html'
    success_url = reverse_lazy('home')


class BlogMusicView(TemplateView):
    model = Post
    template_name = 'music.html'
    success_url = reverse_lazy('home')


class BlogMemView(TemplateView):
    model = Post
    template_name = 'mem.html'
    success_url = reverse_lazy('home')


class BlogMakersView(TemplateView):
    model = Post
    template_name = 'makers.html'
    success_url = reverse_lazy('home')


class BlogNewsView(TemplateView):
    model = Post
    template_name = 'news.html'
    success_url = reverse_lazy('home')


class ProfileView(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)


class EditProfileView(TemplateView):
    template_name = "edit_profile.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.get_profile(request.user))
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, u"Профиль успешно обновлен!")
                return redirect(reverse("profile"))
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None



