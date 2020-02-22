from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post, Comment
from .forms import CommentForm


class PostMaker(CreateView):
	model = Comment
	fields = ['comment', 'comment_author', 'post']

	def get_success_url(self):
		return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class HomeView(TemplateView):
	template_name = 'comments/home.html'


class PostListView(ListView):
	model = Post
	template_name = 'comments/posts_list.html'
	context_object_name = 'posts'


class PostDetailView(DetailView):
	model = Post
	template_name = 'comments/post_detail.html'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(post=self.get_object())
		context['form'] = CommentForm
		return context