from django.http import JsonResponse,HttpResponse

def Response(status_code,message,data=False):
    if status_code and message and (data ):
        result = {
            "status_code":status_code,
            "message":message,
            "data": data
        }

        return HttpResponse(JsonResponse(result),status=status_code,content_type='application/json; charset=UTF-8')
    elif status_code and message:
        result = {
            "status_code": status_code,
            "message": message
        }

        print(result)
        return HttpResponse(JsonResponse(result),status=status_code,content_type='application/json; charset=UTF-8')