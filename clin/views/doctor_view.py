from clin.managers import doctor_manager
from clin.responses import success_json_response


def get_doctors_by_uname(uname):
    doctors = doctor_manager.get_doctors_by_uname(uname)
    return success_json_response({'doctors': doctors})