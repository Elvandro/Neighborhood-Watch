from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile, Neighbourhood, Join, Business, Post, Comment
from django.contrib.auth import authenticate
from .forms import CreateHoodForm, CreateBusinessForm, CreatePostForm, CommentForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Neighbourhood.objects.get(pk=request.user.join.hood_id.id)
            posts = Post.objects.filter(hood = request.user.join.hood_id.id)
            business = Business.objects.filter(hood = request.user.join.hood_id.id)
            return render(request, 'hood/myhood.html', {"hood":hood, "posts":posts, "business":business})
        else:
            neighbourhoods = Neighbourhood.objects.all()
            return render(request, 'index.html', {"neighbourhoods":neighbourhoods})



@login_required(login_url='/accounts/login/')
def create_hood(request):
    """
    View to create an instance of a neighbourhood
    """
    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect('index')
    else:
        form = CreateHoodForm()
        return render(request, 'hood/create_hood.html', {"form":form})

@login_required(login_url='/accounts/login/')
def join(request, hoodId):
    """
    View to implement joining a hood
    """
    neighbourhood = Neighbourhood.objects.get(pk=hoodId)
    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
    else:
        Join(user_id=request.user, hood_id=neighbourhood).save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def hood_home(request):
	'''
	This function will retrive instances of a neighbourhood
	'''
	hood = Neighbourhood.objects.filter(user = request.user)
	return render(request,'hood/myhood.html',{"hood":hood})

@login_required(login_url='/accounts/login/')
def exithood(request,hoodId):
	'''
	This function will delete a neighbourhood instance in the join table
	'''
	if Join.objects.filter(user_id = request.user).exists():
		Join.objects.get(user_id = request.user).delete()
		return redirect('index')

@login_required(login_url='/accounts/login/')
def create_business(request):
    '''
    View function to create an instance of a business
    '''
    if Join.objects.filter(user_id = request.user).exists():
        if request.method == 'POST':
            form = CreateBusinessForm(request.POST)
            if form.is_valid():
                business = form.save(commit=False)
                business.user = request.user
                business.hood = request.user.join.hood_id
                business.save()
                return redirect('hood_home')
        else:
            form = CreateBusinessForm()
            return render(request, 'hood/create_business.html', {"form":form})


@login_required(login_url='/accounts/login/')
def create_post(request):
    '''
    View function to create an instance of a post
    '''
    if Join.objects.filter(user_id = request.user).exists():
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.hood = request.user.join.hood_id
                post.save()
                return redirect('hood_home')
        else:
            form = CreatePostForm()
            return render(request, 'hood/create_post.html', {"form":form})


@login_required(login_url='/accounts/login/')
def create_comment(request, postId):
    '''
    View function to create an instance of a comment
    '''
    if Join.objects.filter(user_id = request.user).exists():
        post = Post.objects.get(id = postId)
        comments = Comment.objects.filter(post = postId)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('hood_home')
        else:
            form = CommentForm()
            return render(request, 'hood/create_comment.html', {"form":form})
