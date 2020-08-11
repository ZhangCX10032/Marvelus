from clin.managers import bill_manager
from clin.responses import success_json_response
import time


def get_bills_by_patient_id(patient_id):
    bills = bill_manager.get_bills_by_patient_id(patient_id)
    return success_json_response({'bills': bills})


def get_all_paid_unpaid_bills_by_doc_uname(uname, paid):
    bills = bill_manager.get_all_paid_unpaid_bills_by_doc_uname(uname, paid)
    return success_json_response({'bills': bills})


def get_all_bills_by_doc_uname(uname):
    bills = bill_manager.get_all_bills_by_doc_uname(uname)
    return success_json_response({'bills': bills})


def get_bill_by_bill_id(bill_id):
    bills = bill_manager.get_bill_by_bill_id(bill_id)
    return success_json_response({'bills': bills})


def add_bill(deal_price, paid, patient_id, uname):
    create_time = time.strftime('%Y-%m-%d %H:%M:%S')
    bills = bill_manager.add_bill(create_time, deal_price, paid, patient_id, uname)
    return success_json_response({'bills': bills})


def set_bill_paid_by_bill_id_and_status(bill_id, paid):
    paid_time = time.strftime('%Y-%m-%d %H:%M:%S')
    bills = bill_manager.set_bill_paid_by_bill_id_and_status(bill_id, paid, paid_time)
    return success_json_response({'bills': bills})
