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

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'recipes': queryset}

    return render(request, 'recipe.html', context)

def update_recipe(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")
        recipe_image = request.FILES.get("recipe_image")

        queryset.receipe_name = recipe_name
        queryset.receipe_description = recipe_desc

        if recipe_image:
            queryset.receipe_image = recipe_image
        
        queryset.save()
        return redirect('/recipe/')

    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)


def delete_recipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')
