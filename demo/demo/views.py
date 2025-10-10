from django.http import HttpResponse

def home(request):
    return HttpResponse("Hii this is welcome page")

def about(request):
    return HttpResponse("Hii this is prahalad here")

def contact(request):
    return HttpResponse("If you are intriested contact me on whatsapp.")

def serveices(request):
    return HttpResponse("We provide web development services, app development services and digital marketing services.")

def products(request):
    return HttpResponse("We provide different types of products like laptops, mobiles, tablets etc.")