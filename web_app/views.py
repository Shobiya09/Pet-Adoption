from django.shortcuts import render
from web_app.filters import DetailFilter
from django.http import HttpResponseRedirect
from web_app.models import Document,Detail
from web_app.forms import DocumentForm,DetailForm
from django.shortcuts import get_object_or_404

def index(request):
    return render(request,'web_app/index.html')

def about(request):
    return render(request,'web_app/about-us.html')

def services(request):
    return render(request,'web_app/services.html')

def blog(request):
    return render(request,'web_app/blog.html')

def contacts(request):
    return render(request,'web_app/contacts.html')

def dogcategory(request):
    context ={'documents':Document.objects.all(),'details':Detail.objects.all()}
    return render(request,'web_app/dog-category.html',context)

def upload_pet(request):
    context ={'documents':Document.objects.all(),'details':Detail.objects.all()}
    return render(request,'web_app/upload-pet.html',context)


def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        form_detail=DetailForm(data=request.POST)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            form_detail.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/upload-pet/')
    else:
        form = DocumentForm() # A empty, unbound form
        form_detail=DetailForm()

    # Load documents for the list page
    documents = Document.objects.all()
    details=Detail.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'web_app/upload.html',
        {'documents': documents, 'form': form,'form_detail':form_detail,'details':details},

    )

def search(request):
    details=Detail.objects.all()
    documents=Document.objects.all()
    Detailfilters = DetailFilter(request.GET, queryset = details)
    return render(request,'web_app/search.html',{'filter': Detailfilters,'documents':documents})

def cat(request):
    details=Detail.objects.all()
    documents=Document.objects.all()
    Detailfilters = DetailFilter(request.GET, queryset = details)
    return render(request,'web_app/cat-category.html',{'filter': Detailfilters,'documents':documents})

def bird(request):
    details=Detail.objects.all()
    documents=Document.objects.all()
    Detailfilters = DetailFilter(request.GET, queryset = details)
    return render(request,'web_app/bird-category.html',{'filter': Detailfilters,'documents':documents})

def edit(request,pk):
    details=get_object_or_404(Detail,pk=pk)
    if request.method == "POST":
        form_detail= DetailForm(request.POST,instance=details)
        if form_detail.is_valid():
            form_detail.save()

            return HttpResponseRedirect('/search/')
    else:
        form_detail=DetailForm(instance=details)

    return render(request,
        'web_app/edit.html',
        { 'form_detail':form_detail},

    )
