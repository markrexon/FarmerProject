from django.db.models.base import Model
from django.views import generic
from .forms import EditProfile
from accounts.models import AddProducts
from .models import Comment,Feedback ,BlogPost
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm, feedBackForm

# Create your views here.

def about(request):
    return render(request,"about.html",{'title': 'About'})

def index(request):
    if not request.user.is_authenticated:
        return render(request,'mainbase.html')
    num_post = BlogPost.objects.filter(author=request.user).count()
    products=AddProducts.objects.all()


    return render(request, 'mainbase.html',{'num_post': num_post})


def LikeView(request,pk):
    post=get_object_or_404(BlogPost,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blogpost:homepage',args=[str(pk)]))

class HomeView(ListView):
    model=BlogPost
    template_name="blog.html"
    

class Addpost(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name="addPost.html"

class ArticleDetail(DetailView):
    model=BlogPost
    template_name="details.html"
    
    def get_context_data(self,*args, **kwargs):

        context = super(ArticleDetail,self).get_context_data(**kwargs)
        stuff= get_object_or_404(BlogPost,id=self.kwargs['pk'])
        total_likes =stuff.total_likes()
        context['total_likes'] = total_likes
        return context

class updatePost(UpdateView):
    model = BlogPost
    template_name="update_post.html"
    fields='__all__'
    
class AddComment(CreateView):
    model = Comment
    form_class=CommentForm
    template_name="addPost.html"
    success_url=reverse_lazy('blogpost:homing')
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def CustomerForm(request):
    form=feedBackForm()
    if request.method=="POST":
        form=feedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogpost:home")
    else:
        form=feedBackForm()

    context ={'form':form}
    return render(request,'feedback.html',context)


class UserChanges(generic.UpdateView):
    form_class = EditProfile
    template_name = "edit_profile.html"
    success_url = reverse_lazy("blogpost:home")

    def get_object(self):
        return self.request.user

