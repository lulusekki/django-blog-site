from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Blog, Category
from . forms import BlogForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'blog/index.html')

class IndexView(TemplateView):
    template_name = 'blog/index.html'

class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
    queryset = Blog.objects.all()
       
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class BlogCreateView(CreateView):

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:create_done')
    def get_context_data(self, **kwargs):
       context = super(BlogCreateView, self).get_context_data(**kwargs)
       context['category_list'] = Category.objects.all()
       context['message_type'] = "create"
       return context
       
def create_done(request):
    #登録処理が正常終了した場合に呼ばれるテンプレートを指定
    category_list = Category.objects.all()  #追加
    return render(request, 'blog/create_done.html',{
        'category_list': category_list })  #category_listを追加
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    def get_context_data(self, **kwargs):
       context = super(BlogDetailView, self).get_context_data(**kwargs)
       context['category_list'] = Category.objects.all()
       return context

class BlogEditView(UpdateView):

    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    
    #登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('blog:edit_done')
    def get_context_data(self, **kwargs):
       context = super(BlogEditView, self).get_context_data(**kwargs)
       context['category_list'] = Category.objects.all()
       context['message_type'] = "edit"
       return context
 
def edit_done(request):
    #更新処理が正常終了した場合に呼ばれるテンプレートを指定
    category_list = Category.objects.all()
    return render(request, 'blog/edit_done.html',{
        'category_list': category_list })