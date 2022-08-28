from django.urls import path
from . import views

urlpatterns = [
    path('getallbuscategory',views.getallbuscategory),
    #path('getbuscategory',views.getbuscategory),
    path('createbuscategory',views.createbuscategory),
    path('updatebuscategory',views.updatebuscategory),
    path('deletebuscategorybyname',views.deletebuscategorybyname),
    path('deletebuscategorybyid/<int:category_id>',views.deletebuscategorybyid),
    
    path('getallbusdetails',views.getallbusdetails),
    path('createabusdetail',views.createabusdetail),
    path('updatebusdetail',views.updatebusdetail),
    path('deletebusdetail',views.deletebusdetail),
    
    path('getbusmodel',views.getbusmodel)
]
