from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Item  # Replace 'Item' with your actual model name
from django.views import View
from .forms import ItemForm

# def item_list(request):
#     """
#     A view to show a list of items.
#     """
#     items = Item.objects.all()
#     context = {'items': items}
#     context = {}
#     return render(request, 'experiments/items.html', context)

"""
CLASS BASED VIEWS
views can be created using functions or classes. Class based views offer more
control over the data processing and rendering
"""
class AddItemView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'experiments/add_item.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list view
        return render(request, 'experiments/add_item.html', {'form': form})

class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'experiments/item_list.html', {'items': items})