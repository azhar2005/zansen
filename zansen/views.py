from django.shortcuts import render
from models import Message

def index(request):
    context = {}
    return render(request, 'index.html', context)
    
def news(request):
    context = {}
    return render(request, 'news.html', context)
    
def msg(request):
    messages = Message.objects.all()
    context = {messages: messages}
    return render(request, 'msg.html', context)
