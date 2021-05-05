from django.shortcuts import render , redirect
from django.views.generic import TemplateView, CreateView, ListView, View
from django.urls import reverse_lazy

# Create your views here.
from .models import PartidoPolitico, Votante, Votacion




class Presentacion(TemplateView):
    template_name = "sistemaVotacion/presentacion.html"



# -------------------------------------------------------------------
# class ListarPartidosPoliticos(TemplateView):
#     template_name = "sistemaVotacion/listarpartidos.html"
    

class ListarPartidosPoliticos(ListView):  # la anterior clase se convierte en una lista 
    model = PartidoPolitico
    template_name = "sistemaVotacion/listarpartidos.html"
    context_object_name = 'partidospoliticos'
# ---------------------------------------------------------------
    
    

# class Votar(TemplateView):
#     template_name = "sistemaVotacion/votar.html"
    


class Votar(CreateView):
    template_name = "sistemaVotacion/votar.html"
    model=Votante
    fields =('__all__')
    success_url = reverse_lazy('urna')
    
    
        
    


# -------------------------------------------------------------------------------------------------
# class Resultados(TemplateView):
#     template_name = "sistemaVotacion/resultados.html"

class Resultados(ListView):
    template_name = "sistemaVotacion/resultados.html"
    model = Votacion # agregar votacion
    context_object_name = 'partidospoliticos'


# -------------------------------------------------------------
# class AltaPartido(TemplateView):
#     template_name = "sistemaVotacion/altapartido.html"


class AltaPartido(CreateView):   # es una evolucion de la clase AltaPartido-TemplateView
    model = PartidoPolitico
    template_name = "sistemaVotacion/altapartido.html"
    fields = ('__all__')
    success_url = reverse_lazy('listarpartidos')
    
# ---------------------------------------------------------------------

# class UrnaView(TemplateView):
    # template_name = "sistemaVotacion/urna.html"


class UrnaView(ListView):
    template_name = "sistemaVotacion/urna.html"
    model = PartidoPolitico
    context_object_name = 'partidospoliticos'



class BotonVotar(View):
    
        
    def dispatch(self, request, *args, **kwargs):
        print(self.kwargs)
        
        pp=PartidoPolitico.objects.get(id=self.kwargs['pk'])
        votacionDePP, _ = Votacion.objects.get_or_create(partidopolitico=pp)
        votacionDePP.numerodevotos =  votacionDePP.numerodevotos + 1
        votacionDePP.save(update_fields=["numerodevotos"])

        
        
        return redirect(reverse_lazy('resultados'))
        # return super().dispatch(request, *args, **kwargs)

    
