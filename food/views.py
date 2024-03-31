from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def recipe(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")
        recipe_image = request.FILES.get("recipe_image")

        Receipe.objects.create(
            receipe_name = recipe_name,
            receipe_description = recipe_desc,
            receipe_image = recipe_image
        )

        return redirect('/recipe/')
    
    queryset = Receipe.objects.all()
    context = {'recipes': queryset}

    return render(request, 'recipe.html', context)

def delete_recipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')
