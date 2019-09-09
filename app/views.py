from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CreateForm
from .models import Post
import datetime
from django.contrib import messages
from django.urls import reverse


# Create your views here.


class IndexView(View):
    def get(self, request):
        today_posts = Post.objects.filter(start_time__date=datetime.date.today()).order_by('start_time')
        tomorrow_posts = Post.objects.filter(start_time__date=(datetime.date.today()+datetime.timedelta(days=1)))\
            .order_by('start_time')
        day_after_tomorrow_posts = Post.objects.filter(start_time__gte=(datetime.date.today()+datetime.timedelta(days=2)))\
            .order_by('start_time')
        return render(request, 'app/index.html', {'today_posts': today_posts, 'tomorrow_posts': tomorrow_posts,
                                                  'day_after_tomorrow_posts': day_after_tomorrow_posts},)


index = IndexView.as_view()


class CreateView(View):
    def get(self, request):
        """GETリクエスト用のメソッド"""
        context = {
            'form': CreateForm()
        }
        return render(request, 'app/create.html', context)

    def post(self, request):
        form = CreateForm(request.POST)
        if not form.is_valid():
            return render(request, 'app/create.html', {'form': form})
        # Post.objects.create(
        #     title=form.title,
        #     start_time=form.start_time,
        #     episode=form.episode,
        #     comment=form.comment
        # )
        # return redirect('app:index')
        post = Post()
        post.title = form.cleaned_data['title']
        post.start_time = form.cleaned_data['start_time']
        post.episode = form.cleaned_data['episode']
        post.comment = form.cleaned_data['comment']

        Post.objects.create(
            title=post.title,
            start_time=post.start_time,
            episode=post.episode,
            comment=post.comment,
        )
        messages.success(request, "投稿しました!")
        return redirect(reverse('app:index'))


create = CreateView.as_view()


class DetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        return render(request, 'app/detail.html', {'post': post})


detail = DetailView.as_view()


class AboutView(View):
    def get(self, request):
        return render(request, 'app/about.html')


about = AboutView.as_view()
