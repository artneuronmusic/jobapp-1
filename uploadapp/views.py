from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadFileForm

# Create your views here.

def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object=form.instance
            return render(request, 'uploadapp/add_img.html', {'form':form, 'saved_object':saved_object})

    else:
        
        form = UploadForm()
    return render(request, 'uploadapp/add_img.html', {'form':form})


def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object=form.instance
            return render(request, 'uploadapp/add_file.html', {'form':form, 'saved_object':saved_object})

    else:
        
        form = UploadFileForm()
    return render(request, 'uploadapp/add_file.html', {'form':form})
