from django.urls import path
from . import views

urlpatterns = [

    path('InsertTrip', views.trip_insert),
    path('getTrip', views.get_trip_details),
    path('getTripbyId/<str:trip_setting_details_id>', views.get_trip_details_id),
    path('delTripbyId/<str:trip_setting_details_id>', views.del_Trip_Details),
    path('tripdetailsinsert', views.tripdetails_insert),
    path('tripdetailsupdate', views.tripdetails_UPDATE),
    path('getdataintrip', views.get_TripDetailsData),
    path('getdatabyid/<str:trip_id>', views.get_trip_detailsData_id),
    path('deldatabyId/<str:trip_id>', views.del_TripDatabyId)
]