from django.conf.urls import include,url
from django.contrib import admin
from . import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from django.conf import settings

from nettest.views import FileDetailView,FileEventView ,EventDetailView , SimulateView


urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^registerini/',views.register,name='registerini'),
    url(r'^register/',views.register,name='register'),

    url(r'^upload/',views.upload,name='upload'),
    url(r'^graphs/',views.graphs,name='graphs'),
    url(r'^simparam/',views.simparam,name='simparam'),
    url(r'^comparegraph/',views.comparegraph,name='comparegraph'),
    url(r'^livegraphs/',views.livegraphs,name="livegraphs"),
    url(r'^searchini/',views.searchini,name='searchini'),
    url(r'^searchwithid/',views.searchwithid,name='searchwithid'),
    url(r'^captureini/',views.captureini,name='captureini'),
    url(r'^simulate/',SimulateView.as_view(),name='simulate'),
    url(r'^admin/',views.admin,name='admin'),
    url(r'^execute/',views.execute,name='execute'),
    url(r'^searcheve/',views.searchevent,name='search'),
    url(r'^captureini/',views.captureini,name='captureini'),
    url(r'^capture/',views.capture,name='capture'),

    url(r'^manage/',views.manage,name='manage'),
    url(r'^deleterow/',views.deleterow,name='deleterow'),
    url(r'^updaterow/',views.updaterow,name='updaterow'),
    url(r'^deleteall/',views.deleteall,name='deleteall'),

    url(r'^nara/',views.nara),
    url(r'^narayan/',views.narayan),

    url(r'^generalsettings/',views.generalsettings),
    url(r'^configure/',views.configure),
    url(r'^configureinterfaces/',views.configureinterfaces),


    url(r'^deletesettings/',views.deletesettings), 
    url(r'^selecttoaddscanned/',views.selecttoaddscanned),
    url(r'^scanclienttodatabase',views.scanclienttodatabase),
    url(r'^selecttomonitor/',views.selecttomonitor),
    url(r'^addclienttoselecttomonitor/',views.addclienttoselecttomonitor),
    url(r'^showmonitorform/',views.showmonitorform),   

    url(r'^selecttosimulate/',views.selecttosimulate),
    url(r'^addclienttoselecttosimulate/',views.addclienttoselecttosimulate),
    url(r'^showsimulationform/',views.showsimulationform),
    url(r'^store/',views.store,name='store'),
 
    url(r'^executetsharkmonitor',views.executetsharkmonitor),
    url(r'^executetshark/',views.executetshark),
    url(r'^$',views.index),
]+  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
