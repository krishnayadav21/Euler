from email import message
from pickle import FALSE, TRUE
from sre_parse import FLAGS
from unicodedata import category
from django.shortcuts import render
from django.core import serializers
from BusApp.models import Category,BusDetails
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
from datetime import datetime
import json
from BusApp.customresponse import Response

#get all bus category
def getallbuscategory(request):
    data=Category.objects.filter(is_deleted=False).order_by('category_id')
    if data:
        Result=json.loads(serializers.serialize("json",data))
        Resultlist=[]
        for i in Result:
            data1=i['fields']['category_name']
            Resultlist.append(data1)
        return HttpResponse(Response(HTTPStatus.OK,"Record Fetch Successfully",Resultlist),content_type="json")
    else:
        return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record not Found"),content_type="json")

#create new bus category
@csrf_exempt
def createbuscategory(request):
    request_body=json.loads(request.body)
    if 'category_id' in request_body and request_body['category_id'] and 'category_name' in request_body and request_body['category_name'] and 'created_by' in request_body and request_body['created_by']:
        if request_body['category_id']>=0: 
            data_exist=Category.objects.filter(category_id=request_body['category_id']).exists()
            if not data_exist:
                newdata=Category(category_id=request_body['category_id'],category_name=request_body['category_name'],
                created_by=request_body['created_by'],created_date_time=datetime.now())
                newdata.save()
                return HttpResponse(Response(HTTPStatus.CREATED,"Record Inserted Successfully"),content_type="json")
            else:
                return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record Already Exists againts the category_id"),content_type="json")
        else:
            return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Number should be greater then zero"),content_type="json")    
    else:
        return HttpResponse(Response(HTTPStatus.BAD_REQUEST,"field should not empty or request body is not proper"),content_type="json")

@csrf_exempt
def updatebuscategory(request):
    request_body=json.loads(request.body)
    if 'category_id' in request_body and request_body['category_id'] and 'category_name' in request_body and request_body['category_name'] and 'modified_by' in request_body and request_body['modified_by']:
        if request_body['category_id']>=0: 
            data_exist=Category.objects.filter(category_id=request_body['category_id']).exists()
            if data_exist:
                data=Category.objects.filter(category_id=request_body['category_id']).update(category_name=request_body['category_name'],
                modified_by=request_body['modified_by'],modified_date_time=datetime.now())
                if data:
                    return HttpResponse(Response(HTTPStatus.OK,"Record Updated Successfully"),content_type="json")
                else:
                    return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record Failed to Update"),content_type="json")    
            else:
                return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Data not exist againts the category_id"),content_type="json")
        else:
            return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Number should be greater then zero"),content_type="json")    
    else:
        return HttpResponse(Response(HTTPStatus.BAD_REQUEST,"field should not empty or request body is not proper"),content_type="json")

@csrf_exempt
def deletebuscategorybyname(request):
    request_body=json.loads(request.body)
    if 'category_name' in request_body and request_body['category_name']:
        data_exist=Category.objects.filter(category_name=request_body['category_name'],is_deleted=False).exists()
        if not data_exist:
            return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Data not exist againts the category_name"),content_type="json")
        else:
            Result=Category.objects.filter(category_name=request_body['category_name']).update(is_deleted=True)
            if Result:
                return HttpResponse(Response(HTTPStatus.NO_CONTENT,"Record Deleted Successfully"),content_type="json")
            else:
                return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record Failed to Delete"),content_type="json")    
    else:
        return HttpResponse(Response(HTTPStatus.BAD_REQUEST,"field should not empty or request body is not proper"),content_type="json")

@csrf_exempt
def deletebuscategorybyid(request,category_id):
    data_exist=Category.objects.filter(category_id=category_id,is_deleted=False).exists()
    if not data_exist:
        return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Data not exist againts the category_id"),content_type="json")
    else:
        Result=Category.objects.filter(category_id=category_id).update(is_deleted=True)
        if Result:
            return HttpResponse(Response(HTTPStatus.NO_CONTENT,"Record Deleted Successfully"),content_type="json")
        else:
            return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record Failed to Update"),content_type="json")    
            

def getallbusdetails(request):
    data=BusDetails.objects.filter(is_deleted=False)
    if data:
        Result=json.loads(serializers.serialize("json",data))
        return HttpResponse(Response(HTTPStatus.OK,"Record Fetch Successfully",Result),content_type="application/json")
    else:
        return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record not Found"),content_type="json")

@csrf_exempt
def createabusdetail(request):
    request_body=json.loads(request.body)
    if 'vin' in request_body and request_body['vin'] and 'vehicle_id' in request_body and request_body['vehicle_id'] and 'model_number'in request_body and request_body['model_number'] and 'model' in request_body and request_body['model'] and 'fuel_type' in request_body and request_body['fuel_type'] and 'number_seats' in request_body and request_body['number_seats'] and 'category_id' in request_body and request_body['category_id'] and 'created_by' in request_body and request_body['created_by']:
        if request_body['category_id']>=0 and request_body['vin']>=0 and request_body['number_seats']>=0: 
            data_exist=BusDetails.objects.filter(vin=request_body['vin']).exists()
            if not data_exist:
                category=Category.objects.get(category_id = request_body['category_id'])
                if category:
                    return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"This is not valid category"),content_type="json")
                else:
                    newdata=BusDetails(vin=request_body['vin'],vehicle_id=request_body['vehicle_id'],model_number=request_body['model_number'],
                    model=request_body['model'],fuel_type=request_body['fuel_type'],number_seats=request_body['number_seats'],category = category,
                    craeted_by=request_body['craeted_by'],created_date_time=datetime.now())
                    newdata.save()
                    return HttpResponse(Response(HTTPStatus.CREATED,"Record Inserted Successfully"),content_type="json")
            else:
                return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Record Already Exists againts the vin"),content_type="json")
        else:
            return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Number should be greater then zero"),content_type="json")    
    else:
        return HttpResponse(Response(HTTPStatus.BAD_REQUEST,"field should not empty or request body is not proper"),content_type="json")

@csrf_exempt
def updatebusdetail(request):        
    request_body=json.loads(request.body)
    data_exist=BusDetails.objects.filter(vin=request_body['vin']).exists()
    if not data_exist:
        return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Data not exist againts the vin"),content_type="json")
    else:
        data=BusDetails.objects.filter(vin=request_body['vin']).update(vehicle_id=request_body['vehicle_id'],model_number=request_body['model_number'],
        model=request_body['model'],fuel_type=request_body['fuel_type'],number_seats=request_body['number_seats'],category=request_body['category_id'],
        modified_by=request_body['modified_by'],is_deleted=request_body['is_deleted'],modified_date_time=datetime.now())
        return HttpResponse(Response(HTTPStatus.OK,"Record Updated Successfully"),content_type="json")

@csrf_exempt
def deletebusdetail(request):
    request_body=json.loads(request.body)
    count=BusDetails.objects.filter(vin=request_body['vin'], is_deleted=False).count()
    if count==0:
        return HttpResponse(Response(HTTPStatus.INTERNAL_SERVER_ERROR,"Data not exist againts the vin"),content_type="json")
    else:
        Result=BusDetails.objects.filter(vin=request_body['vin']).update(is_deleted=request_body['is_deleted'])
        return HttpResponse(Response(HTTPStatus.NO_CONTENT,"Record Deleted Successfully"),content_type="json")

@csrf_exempt
def getbusmodel(request):
    request_body=json.loads(request.body)
    data=BusDetails.objects.filter(category=request_body['category_id'])
    Results=json.loads(serializers.serialize("json",data))
    newrecordslist=[]
    for result in Results:
        record=result['fields']['model']
        newrecordslist.append(record)
    return HttpResponse(Response(HTTPStatus.OK,"Record Fetch Successfully",newrecordslist),content_type="json")
