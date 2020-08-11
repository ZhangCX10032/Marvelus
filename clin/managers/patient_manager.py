from clin import sql_helper


def get_patients_by_name(name):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM Patients p WHERE p.name = %(name)s",
        {'name': name})


def get_patients_by_patient_id(patient_id):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM Patients WHERE patient_id = %(patient_id)s",
        {'patient_id': patient_id}
    )


def get_all_patients():
    return sql_helper.fetchall_to_dict("SELECT * FROM Patients")


def search_patients(keyword):
    return sql_helper.fetchall_to_dict("SELECT * FROM Patients p WHERE p.name LIKE %(keyword)s",
                                       {"keyword": '%' + keyword + '%'})


def add_patient(birthdate, name, phone_number):
    last_id = sql_helper.insert_and_return_id("INSERT IGNORE INTO Patients values"
                                    " (NULL, %(birthdate)s, %(name)s, %(phone_number)s)",
                                    {'birthdate': birthdate, 'name': name, 'phone_number': phone_number})

    return get_patients_by_patient_id(last_id)
