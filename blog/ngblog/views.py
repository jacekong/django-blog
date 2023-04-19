from django.shortcuts import render,redirect
from django.views import View
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.core.paginator import Paginator
from .models import Category
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
class Index(View):
    def get(self, request):
        # post = Post.objects.all()
        posts = Post.objects.order_by('-created').exclude()[:4]
        context = {'posts': posts}
        return render(request, 'index.html', context)

class Content(View):
    def get(self, request):
        # posts
        article = Post.objects.all().order_by('-created')
        paginator  = Paginator(article, 8)
        
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        
        # categories
        cats = Category.objects.all()
        
        cat_id = request.GET.get('cats')
        if cat_id:
            posts = Post.objects.filter(category = cat_id)
        
        context = {
            'posts': posts,
            'cats': cats
        }
        
        return render(request, 'content.html', context)

class About(View):
    def get(self, request):
        return render(request, 'about.html')
    
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html') 

class DetatiledPage(View):
    def get(self, request, slug):
        d_post = Post.objects.get(slug=slug)
        d_posts = Post.objects.order_by('-created').exclude(post_id__exact=d_post.post_id)[:4]
            #get four newest posts
        context = {'post': d_post, 'posts': d_posts}
        return render(request, 'blogpage.html', context)  

@login_required
def createPost(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    if not request.user.is_authenticated:
        raise Http404
    
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post.title, allow_unicode=True) + slugify(post.post_id)
            post.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'create.html', context)

@login_required
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('details', slug=post.slug)
    context = {'form':form}
    return render(request, 'create.html', context)

@login_required
def admin_view(request):
    return render(request, 'admin.html', {})