from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    text = """Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quam doloremque, inventore soluta perferendis dolorum minus vel ad ab, dolore quaerat, rerum quidem. Nobis nam perspiciatis ipsa quasi libero consequatur asperiores."""

    vegetables = ["tomato", "onion", "cabbage"]

    return render(request, 'home/index.html', context={'text': text, 'vegetables':vegetables})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')