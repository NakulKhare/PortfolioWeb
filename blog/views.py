from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.
def allBlogs(request):
    return render(request, "blogs/allblog.html", {"blogObj":Blog.objects})


# for handle this we add => from django.shortcuts import render, get_object_or_404
def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, "blogs/detail.html", {"blogDetail":detail_blog})