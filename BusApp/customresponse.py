from django.http import JsonResponse
def Response(statuscode,message,data=""):
    if statuscode and message and data:
        Result={"status":statuscode,"message":message,"data":data}
    else:
        Result={"status":statuscode,"message":message}
    return JsonResponse(Result)