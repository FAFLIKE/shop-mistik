from django.shortcuts import render

def mainPage(request):
    x = '1'
    context = {'Number': x}
    return render(request, 'tovar/main_page.html', context)
    