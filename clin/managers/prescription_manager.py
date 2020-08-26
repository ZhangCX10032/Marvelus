from clin import sql_helper


def get_prescriptions_with_medicine_by_patient_name(patient_name):
    return sql_helper.fetchall_to_dict(
        "SELECT uname, patient_id, create_time, prescription_id, med_name, med_manufacturer, brand, spec, name, phone_number"
        " FROM ((Patients NATURAL JOIN Prescriptions) NATURAL JOIN Has_Medicine) p WHERE p.name = %(name)s"
        " ORDER BY patient_id DESC",
        {'name': patient_name})


def get_prescriptions_with_medicine_by_patient_id(patient_id):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM Prescriptions NATURAL JOIN Has_Medicine WHERE patient_id = %(patient_id)s ORDER BY create_time",
        {'patient_id': patient_id})


def get_prescription_with_medicine_by_prescription_id(prescription_id):
    return sql_helper.fetchone_to_dict("SELECT * FROM Prescriptions NATURAL JOIN Has_Medicine"
                                       " WHERE prescription_id = %(prescription_id)s",
                                       {'prescription_id': prescription_id})


def get_prescription_by_prescription_id(prescription_id):
    return sql_helper.fetchone_to_dict("SELECT * FROM Prescriptions WHERE prescription_id = %(prescription_id)s",
                                       {'prescription_id': prescription_id})


def add_prescription(create_time, uname, patient_id, content):
    last_id = sql_helper.insert_and_return_id("INSERT IGNORE INTO Prescriptions"
                                              " values (null, %(create_time)s, %(uname)s, %(patient_id)s, %(content)s)",
                                              {'create_time': create_time, 'uname': uname, 'patient_id': patient_id,
                                               'content': content})

    return get_prescription_by_prescription_id(last_id)


def add_medicine_to_prescription(prescription_id, med_name, med_manufacturer, brand, spec, amount):
    return sql_helper.exec_sql("INSERT IGNORE INTO Has_Medicine "
                               " (prescription_id, med_name, med_manufacturer, brand, spec, amount)"
                               " values %(prescription_id)s, %(med_name)s,"
                               " %(med_manufacturer)s, %(brand)s, %(spec)s, %(amount)s",
                               {'prescription_id': prescription_id, 'med_name': med_name,
                                'med_manufacturer': med_manufacturer, 'brand': brand, 'spec': spec, 'amount': amount})
