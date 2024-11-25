from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DeleteView

from forumApp.posts.forms import PostDeleteForm, PostCreateForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


# Create your views here.
class BaseView:
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)


class IndexView(TemplateView):
    # template_name = 'common/index.html'     #   Static way
    extra_context = {
        'static_time': datetime.now()
    } # Static way - Not changed

    def get_context_data(self, **kwargs): # Dynamic way - Changed every time when refresh
        context = super().get_context_data(**kwargs)
        context['dynamic_time'] = datetime.now()
        return context

    def get_template_names(self):   # Dynamic way
        if self.request.user.is_authenticated:
            # return ['posts/dashboard.html']
            return ['common/index_login.html']
        else:
            return ['common/index.html']


class Index(BaseView):
    def get(self, request, *args, **kwargs):

        context = {
            'dynamic_time': datetime.now(),
        }

        return render(request, 'common/index.html', context)


# def index(request):
#     post_form = modelform_factory(
#         Post,
#         fields=('title', 'content', 'author', 'languages' ),
#     )
#
#     context = {
#         "my_form": post_form,
#     }
#
#     return render(request, 'common/index.html', context)


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'   # for post in posts in dashboard.html
    form_class = SearchForm     # Search form
    success_url = reverse_lazy('dashboard') # redirect to dashboard from Search Form
    model = Post

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     form = self.form_class(self.request.GET)
    #     if form.is_valid():
    #         query = form.cleaned_data['query']
    #         queryset = queryset.filter(title__icontains=query)
    #     return queryset

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-created_at')

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = self.queryset.filter(title__icontains=query)

        return queryset



# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all().order_by('-id')
#
#     if request.method == 'GET':
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dashboard')


# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/add-post.html', context)


class DeletePostView(DeleteView):
    model = Post
#    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    # context_object_name = 'post'
    success_url = reverse_lazy('dashboard')


    # Show form fields for editing
    # def get_initial(self):
    #     pk = self.get_object().id
    #     post = Post.objects.get(pk=pk)
    #     initial_data = post.__dict__
    #
    #     if hasattr(post, 'image') and post.image:
    #         initial_data['image'] = post.image.url
    #
    #     return initial_data



# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, 'posts/delete-post.html', context)



class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages', 'image'))
        else:
            return modelform_factory(Post, fields=( 'title', 'content',))


# def edit_post(request, pk: int):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == "POST":
#         form = PostEditForm(request.POST, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, 'posts/edit-post.html', context)


def details_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        "formset": formset,
    }

    return render(request, 'posts/details-post.html', context)



class RedirectHomeView(RedirectView):
    url = reverse_lazy('index') # Static way

    # def get_redirect_url(self, *args, **kwargs):  # Dynamic way
    #     pass

