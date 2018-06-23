from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponseRedirect,redirect
from django.contrib import messages
from .models import Post
from .form import PostForm

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Sucessfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Sucessfully Not Created")
    context={
        "form":form,
    }
    return render(request, "forms.html",context)


def post_detail(request,id=None):  # retrieve
    instance= get_object_or_404(Post,id=id)
    context = {
        "title":instance.title,
        "instance":instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):  # list_items
    # ereturn HttpResponse("<h1>list</h1>")
    queryset=Post.objects.all()
    context={
        "object_list":queryset
    }
    return render(request, "index.html",context)


def post_update(request ,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Sucessfully Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Sucessfully Not Edited")

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "forms.html", context)



def post_delete(request,id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    return redirect("posts:post_list")



