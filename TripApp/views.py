from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
from TripApp.responsemessage import Response
from .models import Trip_Master_TripDetails, Trip_Master_TripSettingDetails


@csrf_exempt
def trip_insert(request):
    if request.method == 'POST':

        requestbody = json.loads(request.body)

    Trip_insert_List = Trip_Master_TripSettingDetails(
        trip_setting_details_id=requestbody['trip_setting_details_id'],
        repeat_on=requestbody['repeat_on'],
        repeat_start_date=requestbody['repeat_start_date'],
        repeat_end_date=requestbody['repeat_end_date'],
        trip_start_time=requestbody['trip_start_time'],
        pricing_per_km=requestbody['pricing_per_km'],
        is_deleted=requestbody['is_deleted']
    )
    try:
        Trip_insert_List.save()
        return Response(HTTPStatus.CREATED, "DATA UPDATED SUCCESFULLY")
    except:
        return Response(HTTPStatus.INTERNAL_SERVER_ERROR, "DATA NOT UPDATED SUCCESFULLY")


def get_trip_details(request):
    if request.method == 'GET':
        try:
            trip = Trip_Master_TripSettingDetails.objects.all().values()
            res = Response(
                HTTPStatus.OK, "DATA Fetch Successfully", list(trip))
        except:
            res = Response(HTTPStatus.INTERNAL_SERVER_ERROR,"DATA NOT Fetched SUCCESFULLY")
    return res
        


def get_trip_details_id(request, trip_setting_details_id):
    if request.method == 'GET':
        try:
            trip = Trip_Master_TripSettingDetails.objects.filter(
                trip_setting_details_id=trip_setting_details_id).values()
            res = Response(
                HTTPStatus.OK, "DATA Fetch Successfully", list(trip))
        except:
            res = Response(HTTPStatus.INTERNAL_SERVER_ERROR,"DATA NOT Fetched SUCCESFULLY")
    return res


@csrf_exempt
def del_Trip_Details(request, trip_setting_details_id):
    if request.method == 'DELETE':
        try:
            coll = Trip_Master_TripSettingDetails.objects.filter(
                trip_setting_details_id=trip_setting_details_id)
            coll.delete()
            res = Response(HTTPStatus.OK, "DATA DELETED Successfully",)
        except:
            res = Response(HTTPStatus.INTERNAL_SERVER_ERROR,"DATA NOT DELETED ")
    return res

# post data in trip details:
@csrf_exempt
def tripdetails_insert(request):
    try:
        requestbody = json.loads(request.body)
        data = Trip_Master_TripSettingDetails.objects.get(
            trip_setting_details_id=requestbody['trip_settings_fk'])

        objectData = {
            "trip_id": requestbody["trip_id"],
            "fleet_id": requestbody["fleet_id"],
            "vehicle_id": requestbody["vehicle_id"],
            "driver_id": requestbody["driver_id"],
            "trip_settings_fk": data,
            "start_date_time": requestbody["start_date_time"],
            "end_date_time": requestbody["end_date_time"],
            "trip_status": requestbody["trip_status"],
            "is_cancel": requestbody["is_cancel"],
            "is_deleted": requestbody["is_deleted"]
        }

        Trip_insert_List = Trip_Master_TripDetails(**objectData)
        Trip_insert_List.save()
        return Response(HTTPStatus.CREATED, "DATA UPDATED SUCCESFULLY")
    except Exception as error:
        print(error)
        return Response(HTTPStatus.INTERNAL_SERVER_ERROR, "DATA NOT UPDATED SUCCESFULLY")



# UPDATE DATA ACCORDING in tripdetails:-
@csrf_exempt
def tripdetails_UPDATE(request):
    if request.method == 'UPDATE':

        requestbody = json.loads(request.body)
        data = Trip_Master_TripSettingDetails.objects.get(
            trip_setting_details_id=requestbody['trip_settings_fk'])
        Trip_Master_TripDetails.objects.get(
            trip_id=requestbody['trip_id']).update(
            trip_id=requestbody["trip_id"],
            fleet_id=requestbody["fleet_id"],
            vehicle_id=requestbody["vehicle_id"],
            driver_id=requestbody["driver_id"],
            trip_settings_fk=data,
            start_date_time=requestbody["start_date_time"],
            end_date_time=requestbody["end_date_time"],
            trip_status=requestbody["trip_status"],
            is_cancel=requestbody["is_cancel"],
            is_deleted=requestbody["is_deleted"]
        )
        
        return Response(HTTPStatus.CREATED, "DATA UPDATED SUCCESFULLY")
    else:
        return Response(HTTPStatus.INTERNAL_SERVER_ERROR, "DATA NOT UPDATED SUCCESFULLY")



# # get data in trip details:
def  get_TripDetailsData(request):
    if request.method == 'GET':
        try:
            trip = Trip_Master_TripDetails.objects.all().values()
            res = Response(HTTPStatus.OK, "DATA Fetch Successfully", list(trip))
        except:
            res = Response(HTTPStatus.INTERNAL_SERVER_ERROR, "DATA NOT Fetched SUCCESFULLY")
    return res

# get trip details data by id:

def get_trip_detailsData_id(request, trip_id):
    if request.method == 'GET':
        try:
            trip = Trip_Master_TripDetails.objects.filter(
                trip_id=trip_id).values()
            res = Response(
                HTTPStatus.OK, "DATA Fetch Successfully", list(trip))
        except:
            res = Response(HTTPStatus.INTERNAL_SERVER_ERROR,"DATA NOT Fetched SUCCESFULLY")
    return res


# Data deleted by Id on TripDetails:
@csrf_exempt
def del_TripDatabyId(request, trip_id):
    if request.method == 'DELETE':
        try:
            trip = Trip_Master_TripDetails.objects.filter(trip_id=trip_id)
            trip.delete()
            res = Response(HTTPStatus.OK, "DATA DELETED Successfully",)
        except:
            res = Response(HTTPStatus.INTERNAL_SERVER_ERROR,"DATA NOT DELETED ")
    return res






@csrf_exempt
def tripdetails_UPDATE(request):
    if request.method == 'UPDATE':

        requestbody = json.loads(request.body)
        data = Trip_Master_TripSettingDetails.objects.get(
            trip_setting_details_id=requestbody['trip_settings_fk'])
        Trip_Master_TripDetails.objects.get(
            trip_id=requestbody['trip_id']).update(
            trip_id=requestbody["trip_id"],
            fleet_id=requestbody["fleet_id"],
            vehicle_id=requestbody["vehicle_id"],
            driver_id=requestbody["driver_id"],
            trip_settings_fk=data,
            start_date_time=requestbody["start_date_time"],
            end_date_time=requestbody["end_date_time"],
            trip_status=requestbody["trip_status"],
            is_cancel=requestbody["is_cancel"],
            is_deleted=requestbody["is_deleted"]
        )
        
        return Response(HTTPStatus.CREATED, "DATA UPDATED SUCCESFULLY")
    else:
        return Response(HTTPStatus.INTERNAL_SERVER_ERROR, "DATA NOT UPDATED SUCCESFULLY")