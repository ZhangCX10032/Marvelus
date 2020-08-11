from clin.managers import bp_record_manager
from clin.responses import success_json_response

def get_bp_records_by_patient_id(patient_id):
    bp_records = bp_record_manager.get_bp_records_by_patient_id(patient_id);
    return success_json_response({'bp_records': bp_records})
