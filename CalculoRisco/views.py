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
        
        imc = request.POST.get('imc','')
        circunferencia_abdominal = request.POST.get('circunferencia_abdominal','')
        altura = request.POST.get('altura','')
        raca_cor = request.POST.get('raca_cor','')
        raca_cor = request.POST.get('raca_cor','')
        
        pressao_arterial_sistolica = request.POST.get('pressao_arterial_sistolica')
        pressao_arterial_diastolica = request.POST.get('pressao_arterial_diastolica')
        
        #SEÇÃO 1
        sexo = request.POST.get('sexo','')
        idade = request.POST.get('idade','')
        historico_dcv = request.POST.get('historico_dcv','')
        tabagismo = request.POST.get('tabagismo','')
        diabetes = request.POST.get('diabetes','')
        obesidade = request.POST.get('obesidade','')
        dislipidemia = request.POST.get('dislipidemia','')
        
        #SEÇÃO 2
        hipertrofia_ventricular = request.POST.get('hipertrofia_ventricular','')
        microalbuminuria = request.POST.get('microalbuminuria','')
        doenca_renal_cronica = request.POST.get('doenca_renal_cronica','')
        indice_tornozelo = request.POST.get('indice_tornozelo','')
        espessura_mediointimal = request.POST.get('espessura_mediointimal','')
        
        # SEÇÃO 3
        ave_isquêmico = request.POST.get('ave_isquêmico','')
        hemorragia_cerebral = request.POST.get('hemorragia_cerebral','')
        ataque_isquemico = request.POST.get('ataque_isquemico','')
        angina_estavel = request.POST.get('angina_estavel','')
        infarto_miocardio = request.POST.get('infarto_miocardio','')
        revascularizacao_miocardio = request.POST.get('revascularizacao_miocardio','')
        clinica_insuficiencia_cardiaca = request.POST.get('clinica_insuficiencia_cardiaca','')
        doenca_arterial_periferica = request.POST.get('angina_estavel','')
        doenca_estagio_4 = request.POST.get('doenca_estagio_4','')
        retinopatia_avancada = request.POST.get('retinopatia_avancada','')
        

        lista_secao_1 = [sexo,idade,historico_dcv,tabagismo,diabetes,obesidade,dislipidemia]
        lista_secao_2 = [hipertrofia_ventricular,microalbuminuria,doenca_renal_cronica,indice_tornozelo,espessura_mediointimal]
        lista_secao_3 = [ave_isquêmico,hemorragia_cerebral,ataque_isquemico,angina_estavel,infarto_miocardio,revascularizacao_miocardio,clinica_insuficiencia_cardiaca,doenca_arterial_periferica,doenca_estagio_4,retinopatia_avancada]
        
        quantidade_secao_1 = lista_secao_1.count('Sim')
        quantidade_secao_2 = lista_secao_2.count('Sim')
        quantidade_secao_3 = lista_secao_3.count('Sim')
        
        pressao_arterial_diastolica = int(pressao_arterial_diastolica)
        pressao_arterial_sistolica = int(pressao_arterial_sistolica)
        
        if quantidade_secao_3 >= 1:
            calculo_risco = "RISCO ALTO COM DOENÇA RENAL OU CARDIOVASCULAR ESTABELECIDA"
        elif quantidade_secao_2 >= 1:
            calculo_risco = "RISCO ALTO"
        elif quantidade_secao_1 == 0 and pressao_arterial_sistolica < 130 and pressao_arterial_diastolica < 85 and diabetico == 'Sim':
            calculo_risco = "SEM RISCO"
            
         # SESSOES COM FATOR DE RISCO >=3
        elif quantidade_secao_1 >= 3 and pressao_arterial_sistolica >= 130 and pressao_arterial_sistolica <= 139:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 89:
                calculo_risco = "RISCO MODERADO"
            elif pressao_arterial_diastolica >= 90:
                calculo_risco = "RISCO ALTO"
        
        elif quantidade_secao_1 >= 3 and pressao_arterial_sistolica >= 140:
            if pressao_arterial_diastolica >= 85:
                calculo_risco = "RISCO ALTO"
        
        # SESSOES SEM FATOR DE RISCO, VERIFICAÇÕES PAS E PAD
        elif quantidade_secao_1 == 0 and pressao_arterial_sistolica >= 130 and pressao_arterial_sistolica <= 139:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 89:
                calculo_risco = "SEM RISCO"
            elif pressao_arterial_diastolica >= 90 and pressao_arterial_diastolica <= 99:
                calculo_risco = "RISCO BAIXO"
            elif pressao_arterial_diastolica >= 100 and pressao_arterial_diastolica <= 109:
                calculo_risco = "RISCO MODERADO"
            elif pressao_arterial_diastolica >= 110:
                calculo_risco = "RISCO ALTO"
            
        elif quantidade_secao_1 == 0 and pressao_arterial_sistolica >= 140 and pressao_arterial_sistolica <= 159:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 99:
                calculo_risco = "RISCO BAIXO"
            elif pressao_arterial_diastolica >= 100 and pressao_arterial_diastolica <= 109:
                calculo_risco = "RISCO MODERADO"
            elif pressao_arterial_diastolica >= 110:
                calculo_risco = "RISCO ALTO"
       
        elif quantidade_secao_1 == 0 and pressao_arterial_sistolica >= 160 and pressao_arterial_sistolica <= 179:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 109:
                calculo_risco = "RISCO MODERADO"
            elif pressao_arterial_diastolica >= 110:
                calculo_risco = "RISCO ALTO"                
                
        elif quantidade_secao_1 == 0 and pressao_arterial_sistolica >= 180:
            calculo_risco = "RISCO ALTO"
            
        # SESSOES COM FATOR DE RISCO 1-2
        elif(quantidade_secao_1 == 1 or quantidade_secao_1 == 2) and pressao_arterial_sistolica >= 140 and pressao_arterial_sistolica <= 159:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 99:
                calculo_risco = "RISCO MODERADO"
            elif pressao_arterial_diastolica >= 100 and pressao_arterial_diastolica <= 109:
                calculo_risco = "RISCO ALTO"
            elif pressao_arterial_diastolica >= 110:
                calculo_risco = "RISCO ALTO" 
                   
        elif (quantidade_secao_1 == 1 or quantidade_secao_1 == 2) and pressao_arterial_sistolica >= 130 and pressao_arterial_sistolica <= 139:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 89:
                calculo_risco = "RISCO BAIXO"
            elif pressao_arterial_diastolica >= 90 and pressao_arterial_diastolica <= 99:
                calculo_risco = "RISCO MODERADO"
            elif pressao_arterial_diastolica >= 100:
                calculo_risco = "RISCO ALTO"

        elif (quantidade_secao_1 == 1 or quantidade_secao_1 == 2) and pressao_arterial_sistolica >= 160 and pressao_arterial_sistolica <= 179:
            if pressao_arterial_diastolica >= 85 and pressao_arterial_diastolica <= 110:
                calculo_risco = "RISCO ALTO"
                
        elif (quantidade_secao_1 == 1 or quantidade_secao_1 == 2) and pressao_arterial_sistolica >= 180:
            if pressao_arterial_diastolica >= 85:
                calculo_risco = "RISCO ALTO"

        elif (quantidade_secao_1 == 1 or quantidade_secao_1) == 2 or quantidade_secao_1 >=3:
            if pressao_arterial_sistolica < 130 and pressao_arterial_diastolica < 85 and diabetico == 'Sim':
                calculo_risco = "SEM RISCO"
        
        
                
        context = {
            'calculo_risco': calculo_risco,
        }
        
    return render(request, 'calculo_risco.html', context)