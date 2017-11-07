from string import Template
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import *
from .models import *

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            curr_email = form.cleaned_data['email']
            curr_name = form.cleaned_data['name']
            curr_username = form.cleaned_data['username']
            curr_password = form.cleaned_data['password']
            user_object = User.objects.create_user(first_name=curr_name, username = curr_username, password = curr_password, email = curr_email)
            myuser = MyUser( user = user_object )
            myuser.save()
            return redirect('login')
        else:
            context = {'form':form}
            return render(request, 'index.html', context)
    else:
        if request.user.is_authenticated:
            return redirect('home')
        form = UserForm()
        context = {'form':form}
        return render(request, 'index.html', context)

def home(request):
    #if request.user.is_authenticated:
    return render(request,'home.html')
    #else:
    #    return redirect('login')

def letter(request):
    return render(request,'song_letter.html')


def songList(request):
    if request.method == 'GET': #and request.user.is_authenticated:
        lista_canciones = Song.objects.all()
        context = { 'song_list' : lista_canciones }
        return render(request, 'song_list.html', context)
    return redirect('login')


def individualSong(request, id):
    if request.method == 'GET':
        try:
            current_song = Song.objects.get(pk = id)
        except Song.DoesNotExist:
            raise Http404("Página no encontrada")
        song_letter_html = ""
        indx = 0
        i = 0
        while i < len(current_song.letter):
             if current_song.letter[i] == '{':
                 song_letter_html += "<input type=\"text\" name=\""+ str(indx) + "\" required>"
                 indx += 1
                 i += 2
             else:
                 song_letter_html += current_song.letter[i]
             i+=1
        context = { 'song' : current_song, 'song_letter' : song_letter_html}
        return render(request, 'individual_song.html', context)
    else:
        current_song = Song.objects.get(pk = id)
        complete_options = Option.objects.filter( song = current_song )
        i = 0
        correct = 0
        while i < 10:
            if request.POST[str(i)].lower() == complete_options[i].text.lower():
                correct += 1
            i+=1
        print ("Las correctas son: " + str(correct))
        return render(request, 'home.html')
