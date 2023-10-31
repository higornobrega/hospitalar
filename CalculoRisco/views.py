from django.shortcuts import render


# Create your views here.
def calculo_risco(request):
    context = {
        'calculo_risco': None,
    }
    if request.method == 'POST':
        # request.POST.get('adicione o name do input vindo front', '') 
        hipertenso = request.POST.get('hipertenso', '')
        diabetico = request.POST.get('diabetico', '')
        insulono = request.POST.get('insulono', '')
        amg = request.POST.get('amg', '')
        covid = request.POST.get('covid', '')
        complicacao = request.POST.get('complicacao', '')
        peso = request.POST.get('peso', '')
        
        print(hipertenso)
        print(diabetico)
        print(insulono)
        print(amg)
        print(covid)
        print(complicacao)
        print(peso)
        
        # Faça o calculo de risco 
        calculo_risco = 1
        
        context = {
            'calculo_risco': calculo_risco,
        }
        
    return render(request, 'calculo_risco.html', context)