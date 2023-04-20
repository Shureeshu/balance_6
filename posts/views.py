from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)

    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

def answer(request, post_pk, answer):
    # POST posts/<int:post_pk>/answer/<str:answer>/
    post = Post.objects.get(pk=post_pk)
    user = request.user
    if request.method == "POST":
        if user in post.select1_users.all() or user in post.select2_users.all():
            pass
        else:
            if answer == post.select1_content:
                post.select1_users.add(user)
            elif answer == post.select2_content:
                post.select2_users.add(user)
    return redirect('posts:detail', post_pk)


# jellyfish
    # title = models.CharField(max_length=80)
    # select1_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    # select1_content = models.TextField()
    # select2_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    # select2_content = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    