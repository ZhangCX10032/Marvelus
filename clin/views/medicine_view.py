from clin.managers import medicine_manager
from clin.responses import success_json_response


def get_medicine_by_med_name(med_name):
    medicines = medicine_manager.get_medicine_by_med_name(med_name)
    return success_json_response({'medicines': medicines})

def add_medicine_by_name_manufacturer_brand_spec_amount_default_price(med_name, med_manufacturer, brand, spec,
                                                                      amount, price):
    medicines = medicine_manager.\
        add_medicine_by_name_manufacturer_brand_spec_amount_default_price(med_name, med_manufacturer, brand,
                                                                          spec, amount, price)
    return success_json_response({'medicines': medicines})
