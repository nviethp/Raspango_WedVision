from rest_framework.decorators import api_view
import json
import os
import datetime, time
from dateutil.parser import parse
from api.models import Level, User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from api.apps import *
from django.db.models import Q
from api.views.loginsession import *
from lib.TGMT.TGMTutil import *
from django.conf import settings


####################################################################################################

@api_view(["POST"])           
def DetectObject(request):
    try:
        _token = request.POST.get("token")
        jwt = FindLoginSession(_token)


        dirName = "yolov8"
        _randFilename = GetVNTime().strftime("%Y-%m-%d_%H-%M-%S") + "_" + GenerateRandomString() + ".jpg"
        uploaded_file_abs = os.path.join(settings.MEDIA_ROOT, dirName, _randFilename)
        hasNewImage = SaveImageFromRequest(request, dirName, _randFilename)

        if(not hasNewImage):
            return ErrorResponse("Ảnh không hợp lệ")

        startTime = time.time()

        img = cv2.imread(uploaded_file_abs)
        img, numObjects = settings.YOLO_DETECTOR.Detect(img)

        elapsed = time.time() - startTime
        elapsed = round(elapsed, 2)

        retval, buffer = cv2.imencode('.jpg', img)
        strBase64 = base64.b64encode(buffer)
        
        return Response(
            {'image_base64': strBase64,
             'numObjects': numObjects,
            'elapsed' : elapsed},
            status=SUCCESS_CODE,
            content_type="application/json")

    except Exception as e:
        return ErrorResponse("Có lỗi: " + str(e))
    

