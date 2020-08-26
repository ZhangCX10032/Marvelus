import time
import json

from django.views.decorators.csrf import csrf_exempt
from clin.view_decorators import json_request
from clin.managers import prescription_manager
from clin.responses import success_json_response
from clin.responses import error_json_response

def get_prescriptions_with_medicine_by_patient_name(patient_name):
    prescriptions =  prescription_manager.get_prescriptions_with_medicine_by_patient_name(patient_name)
    return success_json_response({'prescriptions': prescriptions})


def get_prescriptions_with_medicine_by_patient_id(patient_id):
    prescriptions = prescription_manager.get_prescriptions_with_medicine_by_patient_id(patient_id)
    return success_json_response({'prescriptions': prescriptions})


def get_prescription_with_medicine_by_prescription_id(prescription_id):
    prescriptions = prescription_manager.get_prescription_with_medicine_by_prescription_id(prescription_id)
    return success_json_response({'prescriptions': prescriptions})


def get_prescription_by_prescription_id(prescription_id):
    prescriptions = prescription_manager.get_prescription_by_prescription_id(prescription_id)
    return success_json_response({'prescriptions': prescriptions})


@json_request
@csrf_exempt
def add_prescription(request):
    user = request.user
    if user.is_authenticated:
        create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        uname = user.uname
        data = json.loads(request.body)
        prescriptions = prescription_manager.add_prescription(
            create_time, uname, data['patient_id'], data['content'])
        return success_json_response({'prescriptions': prescriptions})
    return error_json_response("用户未登录User not logged in")


@json_request
@csrf_exempt
def add_medicine_to_prescription(request):
    user = request.user
    if user.is_authenticated:
        data = json.loads(request.body)
        added = prescription_manager.\
            add_medicine_to_prescription(data['prescription_id'], data['med_name'], data['med_manufacturer'],
                                         data['brand'], data['spec'], data['amount'])
        return success_json_response({'added': added})
    return error_json_response("用户未登录User not logged in")
