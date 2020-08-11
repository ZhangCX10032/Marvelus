from clin import sql_helper


def get_bills_by_patient_id(patient_id):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM Bills WHERE patient_id = %(patient_id)s ORDER BY create_time DESC",
        {'patient_id': patient_id})

def get_all_paid_unpaid_bills_by_doc_uname(uname, paid):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM Bills WHERE paid = %(paid), uname = %(uname)s ORDER BY create_time",
        {'uname': uname, 'paid': paid})

def get_all_bills_by_doc_uname(uname):
    return sql_helper.fetchall_to_dict(
        "SELECT * FROM Bills WHERE uname = %(uname)s ORDER BY create_time",
        {'uname': uname})

def get_bill_by_bill_id(bill_id):
    return sql_helper.fetchone_to_dict("SELECT * FROM Bills WHERE bill_id = %(bill_id)s", {'bill_id': bill_id})

def add_bill(create_time, deal_price, paid, patient_id, uname):
    last_id = sql_helper.insert_and_return_id(
        "INSERT INTO Bills (bill_id, create_time, paid_time, deal_price, paid, patient_id, uname)"
        " values (NULL, %(create_time)s, NULL, %(deal_price)s, %(paid)s, %(patient_id)s, %(uname)s)",
        {'create_time': create_time, 'deal_price': deal_price, 'paid': paid, 'patient_id': patient_id, 'uname': uname}
    )

    return get_bill_by_bill_id(last_id)

def set_bill_paid_by_bill_id_and_status(bill_id, paid, paid_time):
    return sql_helper.fetchall_to_dict("UPDATE Bills SET paid = %(paid)s"
                                       " WHERE bill_id = %(bill_id)s, paid_time = %(paid_time)s",
                                       {'bill_id': bill_id, 'paid': paid, 'paid_time': paid_time})
