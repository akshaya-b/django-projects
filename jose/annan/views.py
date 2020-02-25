from django.shortcuts import render
from django.http import HttpResponse
from annan.models import AccessRecord, Topic, Website

def index(request):

    website_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':website_list}
    return render(request,'annan/index.html',context=date_dict)
    ## mydict={'one':'Annan','two':', thambi','three':'rendu per'}
    ## return render(request,'annan/index.html',context=mydict)
    # return HttpResponse("Hello World")

# Create your views here.
