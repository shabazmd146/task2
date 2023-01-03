from django.shortcuts import render

# # Create your views here.

# def setsession(request):
#     username = request.session['username']='shabaz'
#     password = request.session['password']='welcome1234'
#     return render(request,'app2/setsession.html',{'username':username,'password':password})



def setsession(request):
    username = request.session['username']='shabaz'
    return render(request,'app2/setsession.html',{'username':username})


def getsession(request):
    # username = request.session.get('username',default='fayaz')
    # password =  request.session.get('password')
    keys = request.session.keys()
    values = request.session.values()
    items = request.session.items()
    contact = request.session.setdefault('contact','123456789')
    return render(request,'app2/getsession.html',{'keys':keys,'values':values,'items':items,'contact':contact})

def delsession(request):
    if 'username' in request.session:
        del request.session['username']
    return render(request,'app2/delsession.html')