from django.shortcuts import render
from django.core.paginator import Paginator
from .models import ObraArte

def album_list(request):
    obras_list = ObraArte.objects.all()
    paginator = Paginator(obras_list, 2)  # 6 obras por página
    
    page_number = request.GET.get('page')
    obras = paginator.get_page(page_number)
    
    context = {
        'obras': obras
    }
    return render(request, 'album/album.html', context)