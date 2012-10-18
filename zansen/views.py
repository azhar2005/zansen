from django.shortcuts import render
from django.http import HttpResponse
from models import Message
from forms import MessageForm
from django.utils import simplejson

def index(request):
    context = {}
    
    return render(request, 'index.html', context)
    
def news(request):
    context = {}
    
    return render(request, 'news.html', context)
    
def msg(request):
    messages = Message.objects.all()
    form = MessageForm()
    print messages
    context = {'messages': messages, 'form': form}
    
    return render(request, 'msg.html', context)
    
def send_msg(request):
    if request.POST:
        form = MessageForm(request.POST)

        if form.is_valid():
            sender = form.cleaned_data['sender']
            text = form.cleaned_data['text']

            new_msg = Message(sender=sender, text=text)
            new_msg.save()

            json = simplejson.dumps({'sender': new_msg.sender, 'text': new_msg.text, 'date': str(new_msg.date)})

            return HttpResponse(json, content_type='application/json')
