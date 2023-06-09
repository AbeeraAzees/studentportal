from django import contrib
from django.shortcuts import redirect, render
from .forms import*
from django.forms.widgets import FileInput
from django.core.checks import messages
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')
def notes(request):
    if request.method =="POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username}successfully")  
    else:
      form = NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")
class NotesDetailView(generic.DetailView):
    model=Notes

def homework(request):
    form=Homeworform()
    homework=Homework.objects.filter(user=request.user)
    if len(homework)==0:
        homework_done =True
    else:
        homework_done=False    
    context={'homeworks':homework,'homeworks_done':homework_done,'form':form}
    return render(request,'dashboard/homework.html',context) 
def youtube(request):
    if request.method == "POST":
        form=DashboardFom(request.POST)
        text=request.POST['text']
        video=VideosSearch(text,limit=10)
        result_list=[]
        for i in video.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['published time'],
            }
            desc=''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc +=j['text']
            result_dict['description']=desc
            result_list.append(result_dict)
            context={
                'form':form,
                'results':result_list
            }
        return render(request,'dashboard/youtube.html',context) 

    else:    
        form=DashboardFom()
    context={'form':form}
    return render(request,"dashboard/youtube.html",context) 
    