from django.shortcuts import render
from .models import Guide
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    print(dict(Guide.objects.all().values()[0]))
    return render(request, 'Nashville/blog-construction.html', {'Guides': Guide.objects.all()})


def view_post(request, slug):
    print('here')
    post = get_object_or_404(Guide, slug=slug)
    return render(request, 'Nashville/blog-single.html', {'post': post
                                                   })
