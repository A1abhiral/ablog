from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Post, Category  # Include your models
from .forms import PostForm, UpdateForm  
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import cloudinary.uploader

# Home view to list all posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()
        return context

# Article Detail view
class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context["cat_menu"] = Category.objects.all()
        context["total_likes"] = post.total_likes()
        context["liked"] = post.likes.filter(id=self.request.user.id).exists()
        return context

# Category view to filter posts
def CategoryView(request, cat):
    category_post = Post.objects.filter(category=cat.replace('-', ' '))
    cat_menu = Category.objects.all()
    return render(request, 'categories.html', {
        'cat': cat.replace('-', ' '),
        'category_post': category_post,
        'cat_menu': cat_menu
    })

# View for liking a post
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

# Create new post
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        # Upload profile picture to Cloudinary
        header_image = form.cleaned_data.get('header_image')  # Ensure 'profile_pic' is the correct field name
        if header_image:
            response = cloudinary.uploader.upload(header_image)
            form.instance.header_image = response['secure_url']  # Store the Cloudinary URL
            
        return super().form_valid(form)


# Update existing post
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "Update_post.html"

    def get_success_url(self):
        return reverse('article-detail', args=[str(self.object.id)])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        # Upload profile picture to Cloudinary
        header_image = form.cleaned_data.get('header_image')  # Ensure 'profile_pic' is the correct field name
        if header_image:
            response = cloudinary.uploader.upload(header_image)
            form.instance.header_image = response['secure_url']  # Store the Cloudinary URL
            
        return super().form_valid(form)

# Delete post
class DeletePostView(DeleteView):
    model = Post
    template_name = "Delete_post.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()
        return context

# Add new category
class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()
        return context
