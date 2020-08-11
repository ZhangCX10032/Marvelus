from clin.managers import prescription_manager
from clin.responses import success_json_response
import time


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

def add_prescription(uname, patient_id):
    create_time = time.strftime('%Y-%m-%d %H:%M:%S')
    prescriptions = prescription_manager.add_prescription(create_time, uname, patient_id)
    return success_json_response({'prescriptions': prescriptions})

def add_medicine_to_prescription(prescription_id, med_name, med_manufacturer, brand, spec, amount):
    added = prescription_manager.add_medicine_to_prescription(prescription_id, med_name, med_manufacturer, brand, spec, amount)
    return success_json_response({'added': added})
