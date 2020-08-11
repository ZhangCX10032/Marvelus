"""EntryTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from clin.views import bill_view, bp_record_view, doctor_view, medicine_view, patient_view, prescription_view, auth_view

from clin import views_helper

urlpatterns = [
    path('login/', auth_view.login),
    path('logout/', auth_view.logout),

    path('doctors/uname/<uname>/', doctor_view.get_doctors_by_uname),

    path('bills/patientid/<patient_id>/', bill_view.get_bills_by_patient_id),
    path('bills/uname/paid/<uname>/<paid>/', bill_view.get_all_paid_unpaid_bills_by_doc_uname),
    path("bills/uname/<uname>/", bill_view.get_all_bills_by_doc_uname),
    path("bills/billid/<bill_id>/", bill_view.get_bill_by_bill_id),
    path("bills/addbill/<deal_price>/<paid>/<patient_id>/<uname>/", bill_view.add_bill),
    path("bills/setpaid/<bill_id>/<paid>/", bill_view.set_bill_paid_by_bill_id_and_status),

    path("medicines/medname/<med_name>/", medicine_view.get_medicine_by_med_name),
    path("medicines/addmed/<med_name>/<med_manufacturer>/<brand>/<spec>/<amount>/<price>/",
         medicine_view.add_medicine_by_name_manufacturer_brand_spec_amount_default_price),

    path("patients/name/<name>/", patient_view.get_patients_by_name),
    path("patients/patientid/<patient_id>/", patient_view.get_patients_by_patient_id),
    path("patients/all/", patient_view.get_all_patients),
    path("patients/search/<keyword>/", patient_view.search_patients),
    path("patients/addpatient/<birthdate>/<name>/<phone_number>/", patient_view.add_patient),

    path("prescriptions/patientname/<patient_name>/",
         prescription_view.get_prescriptions_with_medicine_by_patient_name),
    path("prescriptions/patientid/<patient_id>/", prescription_view.get_prescriptions_with_medicine_by_patient_id),
    path("prescriptions/withmed/prescriptionid/<prescription_id>/",
         prescription_view.get_prescription_with_medicine_by_prescription_id),
    path("prescriptions/prescriptionid/<prescription_id>/", prescription_view.get_prescription_by_prescription_id),
    path("prescriptions/addprescription/<uname>/<patient_id>/", prescription_view.add_prescription),
    path("prescriptions/addmedicinetoprescription/<prescription_id>/"
         "<med_name>/<med_manufacturer>/<brand>/<spec>/<amount>/", prescription_view.add_medicine_to_prescription),

    url(r'', auth_view.default)

    # path('add/', views_helper.add_participator),
]
