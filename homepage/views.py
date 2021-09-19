from django.shortcuts import render
from .models import PixelCounter
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            b_or_w = PixelCounter.black_or_white(self=img_obj)
            users_text = form.cleaned_data['hex_code']
            if PixelCounter.check_hex(users_text):
                rgb = PixelCounter.hex_to_rgb(users_text)
                h = PixelCounter.hex_counter(self=img_obj, rgb_code=rgb)
            else:
                h = '<Hex code отсутствует или неверен>'
            context = {
                'h': h,
                'form': form,
                'img_obj': img_obj,
                'b_or_w': b_or_w,
            }
            return render(request, 'homepage/index.html', context)
    else:
        form = ImageForm()
    return render(request, 'homepage/index.html', {'form': form})

