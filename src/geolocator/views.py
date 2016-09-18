from django.shortcuts import render_to_response, RequestContext

from .functions import locu_search

def home(request):
    if request.method == "POST":
        print request.POST
        query = request.POST['search']
        locu_search(query)


    return render_to_response('home.html', locals(), context_instance=RequestContext(request))