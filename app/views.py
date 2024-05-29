from django.shortcuts import render
import pyshorteners
from django.contrib import messages

# Create your views here.
def home(request):
   try:
        short_url = ""
        url = ""
        if request.method == "POST":
            shortener = pyshorteners.Shortener()
            url = request.POST.get("url")
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Short URL Generated !")
            context = {
                'url':url,
                'short_url':short_url
            }
        return render(request, template_name='home.html',context=context)
   except:
        return render(request, template_name='home.html')
    
