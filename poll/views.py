from multiprocessing import context, pool
from django.shortcuts import render, redirect

from.models import PollQuestion
from .forms import PollForm


# Create your views here.
def create(request):
    if request.method=='POST':
        form=PollForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form=PollForm()

    context={
        'form':form
    }

    return render(request,'create.html',context)


def Homes(request):
    polls=PollQuestion.objects.all()

    context={
        'polls':polls,
        'title':'Poll Application'
    }

    return render(request,'polls.html',context)


def Vote(request,poll_id):
    poll=PollQuestion.objects.get(pk=poll_id)

    if request.method=='POST':
        selected=request.POST['poll']
        print(selected)
        if selected=='option1':
            poll.option_one_count+=1
        elif selected=='option2':
            poll.option_two_count+=1
        elif selected=='option3':
            poll.option_three_count+=1
        elif selected=='option4':
            poll.option_four_count+=1
        else:
            pass
        
        poll.save()
        
    context={'poll':poll}

    return render(request,'Vote.html',context)

def Result(request,poll_id):
    
    poll=PollQuestion.objects.get(id=poll_id)
    context={
        'poll':poll,
    }
    return render(request,'polls.html',context)