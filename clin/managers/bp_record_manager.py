from clin import sql_helper


def get_bp_records_by_patient_id(patient_id):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM BP_Records WHERE patient_id = %(patient_id)s ORDER BY create_time DESC",
        {'patient_id': patient_id})