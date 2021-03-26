
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get text
    djtext = (request.POST.get('text', 'default'))

    #check check checkbox value
    uppercase = request.POST.get('uppercase', 'off')
    removepunc  = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~|'''

    #analyzing text
    analyzed = ''
    if removepunc =='on':

        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

    elif uppercase == 'on':

        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Uppercased ', 'analyzed_text': analyzed}

    elif newlineremover == 'on':

        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed+=char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}

    elif charcount == 'on':
        count = 0
        for i in djtext:
            count+=1
        params = {'purpose': 'Cahracter Count is ...', 'analyzed_text': count}


    else:
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)
