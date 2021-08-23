
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [       
    path('submit_info/<str:id>', submit_info, name='submit_info'),
    path('get_info/<str:id>',get_info,name='get_info'),
    path('get_ieh/<str:id>',get_ieh,name = 'get_ieh'),
    path('disclosure/<str:user_id>/<str:token>/<str:PackageId>/<str:ResidenceState>/<str:TribalResident>/<str:EligibiltyPrograms>', disclosure,name = "disclosure"),
    #path('post/',post_entry),
    path('submit_form/',submit_form, name="submit_form"),
     
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

