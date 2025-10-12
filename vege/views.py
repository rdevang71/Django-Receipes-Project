from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        if receipe_name and receipe_description and receipe_image:
            Recipe.objects.create(
                receipe_name=receipe_name,
                receipe_description=receipe_description,
                receipe_image=receipe_image,
            )
        return redirect('receipes')

    queryset = Recipe.objects.all()
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('receipes')

def update_receipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.receipe_name = request.POST.get('receipe_name')
        recipe.receipe_description = request.POST.get('receipe_description')

        # Only update image if a new one is uploaded
        if request.FILES.get('receipe_image'):
            recipe.receipe_image = request.FILES.get('receipe_image')

        recipe.save()
        return redirect('receipes')

    context = {'recipe': recipe}
    return render(request, 'update_receipe.html', context)