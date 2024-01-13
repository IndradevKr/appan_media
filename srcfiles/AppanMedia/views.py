from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from AppanMedia.models import blogPost, Testimonial
from .forms import ContactForm, CommentForm

# Create your views here.
def index(request):
    testimonials_list= Testimonial.objects.all()
    context ={
        'testimonials_list': testimonials_list,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def thanks(request):
    return render(request, 'thanks.html',)

def about(request):
    return render(request, 'about.html',)

def services(request):
    return render(request, 'services.html', )

def blogs(request):
    context={}
    try:
        blog_list = blogPost.objects.all()
        context['blog_list'] = blog_list
    
    except Exception as e:
        print(e)

    return render(request, 'blogs.html', context)  

def view_blogs(request, slug):
    try:
        blog_obj = blogPost.objects.filter(slug = slug).first()
        post = get_object_or_404(blogPost, slug = slug)
        comments = post.comments.filter(active = True)
        new_comment = None

        #Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data = request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()

        else:
            comment_form = CommentForm()
            
    except Exception as e:
        print(e)

    return render(request, 'view-blogs.html', {'blog_obj':blog_obj, 
                                                'post':post,
                                                'comments':comments,
                                                'new_comment':new_comment,
                                                'comment_form':comment_form})

      