from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Item  # Replace 'Item' with your actual model name


def item_list(request):
    """
    A view to show a list of items.
    """
    # items = Item.objects.all()
    # context = {'items': items}
    context = {}
    return render(request, 'experiments/items.html', context)
