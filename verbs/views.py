from django.shortcuts import render
from django.http import HttpResponse
from . import verbforms as v

# Create your views here.
def index(request):
    return render(request, 'index.html')

def table(request):
    root = request.POST.get('verb')

    # Checks root length
    if not len(root) == 3 * v.char_size:
        return HttpResponse("Not a 3 letter root")

    context = {'root': root, 'past': v.past_tense(root), 'present': v.present_tense}
    return render(request, 'table.html', context)
