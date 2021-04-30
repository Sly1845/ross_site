from django.shortcuts import render
#from django.http import HttpResponse
from . models import Page
def index(request, pagename):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_update': pg.update_date,
	}
    #return HttpResponse("<h1> Meandco Homepage </h1>")
    #assert False
	return render(request, 'pages/page.html', context)
# Create your views here.
