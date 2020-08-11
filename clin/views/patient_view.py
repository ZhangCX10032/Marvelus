from clin.managers import patient_manager
from clin.responses import success_json_response, error_json_response


def get_patients_by_name(request, name):
    if request.user.is_authenticated:
        patients = patient_manager.get_patients_by_name(name)
        return success_json_response({'patients': patients})
    return error_json_response("用户未登录User not logged in")

def get_patients_by_patient_id(request, patient_id):
    if request.user.is_authenticated:
        patients = patient_manager.get_patients_by_patient_id(patient_id)
        return success_json_response({'patients': patients})
    return error_json_response("用户未登录User not logged in")

def get_all_patients(request):
    # print(request)
    if request.user.is_authenticated:
        patients = patient_manager.get_all_patients()
        return success_json_response({'patients': patients})
    return error_json_response("用户未登录User not logged in")

def search_patients(request, keyword):
    if request.user.is_authenticated:
        # TODO: check user role
        return success_json_response({'patients': patient_manager.search_patients(keyword)})
    return error_json_response("用户未登录User not logged in")

def add_patient(birthdate, name, phone_number):
    if request.user.is_authenticated:
        patients = patient_manager.add_patient(birthdate, name, phone_number)
        return success_json_response({'patients': patients})
    return error_json_response("用户未登录User not logged in")
