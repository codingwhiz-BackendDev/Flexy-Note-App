from django.shortcuts import render, redirect
from .models import Note, Alarm
from django.contrib import messages

# Create your views here.

def index(request):
    note = Note.objects.all()
    return render(request,'index.html', {'note':note})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        image = request.FILES.get('image')
        
        note = Note.objects.create(title=title, text=text, image=image)
        note.save();
        messages.info(request, 'Note Added suceessfully')
    
    return render(request,'add.html')
 
def view(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            title = request.POST['title']
            text = request.POST['text'] 
            image = request.FILES.get('image')
            
        
            note.title = title
            note.text = text
            note.image = image 
            note.save() 
            messages.info(request, 'Note Saved suceessfully')
            
        if request.FILES.get('image') == None:
            title = request.POST['title']
            text = request.POST['text']
            
            note.title = title
            note.text = text 
            note.save() 
            messages.info(request, 'Note Saved suceessfully')
    return render(request,'view.html', {'note':note})

def delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('index')
    messages.info(request, 'Note deleted suceessfully')
    return render(request,'view.html', {'note':note})

def alarm(request):
    pass
#     alarm = Alarm.objects.all()
#     if request.method == 'POST':
#         songs = request.FILES.get('songs')
#         caption = request.POST['caption']
#         alarm = Alarm.objects.create(songs=songs, caption=caption)
#         alarm.save()
#         messages.info(request, 'Alarm successfully added')
        
    return render(request,'alarm.html')
 
def delete_image(request, id):
    note = Note.objects.get(id=id)
    note.image.delete()
    return redirect('view.html', {'note':note})