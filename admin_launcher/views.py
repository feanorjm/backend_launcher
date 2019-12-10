from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from django.urls import reverse
from admin_launcher.models import background
from admin_launcher.serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView

from admin_launcher.forms import *


class BackgroundViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = background.objects.all()
    serializer_class = BackgroundSerializer




def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))



#CRUD PARA BACKGROUNDS

'''@method_decorator(login_required, name='dispatch')
class ConductorDetailView(DetailView):
    #context_object_name = "bitacora_detail"
    model = Conductor
    template_name = 'conductor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConductorDetailView, self).get_context_data(**kwargs)
        conductor = self.get_object()
        maquinas = Maquina.objects.filter(compania=conductor.compania)

        maquinas_list = ""
        for maquina in maquinas:
            if conductor in maquina.conductor.all():
                maquinas_list += maquina.nombre+"  "

        context['maquinas_list'] = maquinas_list


        return context

'''

@method_decorator(login_required, name='dispatch')
class BackgroundCreateView(CreateView):
    form_class = BackgroundForm
    template_name = 'app/form_backgrounds.html'

    '''def form_valid(self, form):
        profile_image = Conductor(foto=self.get_form_kwargs().get('files')['foto'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())'''


''' 
@method_decorator(login_required, name='dispatch')
class ConductorListView(ListView):
    #model = Conductor
    template_name = 'conductor_list.html'

    def get_queryset(self):
        today = datetime.now()
        if (self.request.user.usuariocomp.tipo in ('2','3')):
            queryset = Conductor.objects.all().order_by('compania','nombre')
        else:
            user_comp = self.request.user.usuariocomp.compania.pk
            queryset = Conductor.objects.filter(compania=user_comp).order_by('compania','nombre')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ConductorListView, self).get_context_data(**kwargs)
        companias_list = Compania.objects.all()
        if (self.request.user.usuariocomp.tipo not in ('2', '3')):
            user_comp = self.request.user.usuariocomp.compania.pk
            compania_obj = Compania.objects.get(pk=user_comp)
            companias_list = {compania_obj, }

        context['companias_list'] = companias_list
        return context

    def post(self, request, *args, **kwargs):
        compania = self.request.POST.get('compania')
        datos_list = {}
        context = {}

        companias_list = Compania.objects.all()

        if (compania != ''):
            compania_obj = Compania.objects.get(pk=compania)
            datos_list = {'compania':compania_obj.pk}
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                conductores = Conductor.objects.filter(compania=compania_obj).order_by('compania','nombre')


            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                conductores = Conductor.objects.filter(compania=user_comp).order_by('compania','nombre')
                companias_list = {compania_obj,}

        else:
            if (self.request.user.usuariocomp.tipo in ('2','3')):
                conductores = Conductor.objects.all().order_by('compania','nombre')
            else:
                user_comp = self.request.user.usuariocomp.compania.pk
                conductores = Conductor.objects.filter(compania=user_comp).order_by('compania','nombre')
                companias_list = {compania_obj, }

        context['companias_list'] = companias_list
        context['object_list'] = conductores
        context['datos_list'] = datos_list

        return render(request,self.template_name,context=context)

@method_decorator(login_required, name='dispatch')
class ConductorUpdateView(UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = 'conductor_update.html'

@method_decorator(login_required, name='dispatch')
class ConductorDeleteView(DeleteView):
    model = Conductor
    template_name = 'conductor_delete.html'
    success_url = reverse_lazy('conductor_list')

conductor_list = ConductorListView.as_view()
conductor_detail = ConductorDetailView.as_view()
conductor_update = ConductorUpdateView.as_view()
conductor_delete = ConductorDeleteView.as_view()

'''
background_create = BackgroundCreateView.as_view()


