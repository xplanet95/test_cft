from django.shortcuts import render
from .models import PixelCounter
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            red = PixelCounter.black_or_white(self=img_obj)

            context = {
                'form': form,
                'img_obj': img_obj,
                'red': red,
            }
            return render(request, 'homepage/index.html', context)
    else:
        form = ImageForm()
    return render(request, 'homepage/index.html', {'form': form})



# def index(request):
#     if request.method != 'POST' or not request.FILES:
#         file = request.FILES['myfile1']
#         fs = FileSystemStorage()
#         filename = fs.save(file.name, file)
#         file_url = fs.url(filename)
#
#         context = {
#             'file_url': file_url,
#         }
#
#         return render(request, 'home_page.html', context)
#
#
#
#     return render(request, 'homepage/index.html')
    #render(request, 'homepage/index.html', context)

