#I have created this file - Naman
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # return HttpResponse("""<h1>Helloo! Naman singh</h1><a href="https://www.youtube.com/watch?v=RowB5QR_IjY&list=PLjVLYmrlmjGcyt3m6rt21nfjhYSWP_Ue_&index=13" target="_blank"> Django with Naman1</a>,<br>
    # <a href="https://www.youtube.com/watch?v=RowB5QR_IjY&list=PLjVLYmrlmjGcyt3m6rt21nfjhYSWP_Ue_&index=13" target="_blank"> Django with Naman2</a>,<br>
    # <a href="https://www.youtube.com/watch?v=RowB5QR_IjY&list=PLjVLYmrlmjGcyt3m6rt21nfjhYSWP_Ue_&index=13" target="_blank"> Django with Naman3</a>""")

def about(request):
    return HttpResponse(request,"about.html")

def contact(request):
    return HttpResponse(request,"contact.html")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    if removepunc=="on":
        punctuations = '''`~!@#$%^&*()-_'"{}[],.<>/?;:'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    fullcaps = request.POST.get('fullcaps', 'off')
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Capital letters', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    charcount = request.POST.get('charcount', 'off')
    if (charcount=="on"):
        analyzed=len(djtext)
        # for char in range(djtext):
        #     analyzed=analyzed+char.upper()
        params = {'purpose': 'Charcount', 'analyzed_text': ('Numbers of characters in the text is',analyzed)}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("Gandu box pe click kar")

    return render(request, 'analyze.html', params)
        # analyzed=djtext
        # params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
# def address(request):
#     # djtext=request.GET.get('text','default')
#     # addressbatao=request.GET.get('addressbatao','default')
#     # print(addressbatao)
#     # print(djtext)
#     return HttpResponse("""<h1>Narayanpur shivpur varanasi</h1> <a href="/"> <b> Back </b> </a>""")
# def home(request):
#     return HttpResponse("""<h1>Ghar hai naveen upvan k gali me</h1><a href="/"> Back </a>""")
# def gallery(request):
#     return HttpResponse("""<h1>Gallery 9 foot ka hai</h1><a href="/"> Back </a>""")
# def contact(request):
#     return HttpResponse("""<h1>Contact bahut lamba lamba hai</h1><a href="/"> Back </a>""")