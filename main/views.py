from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152342',
        'name': 'Yose Yehezkiel Maranata',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)