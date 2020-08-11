from clin import sql_helper


def get_medicine_by_med_name(med_name):
    return sql_helper.fetchall_to_dict("SELECT * FROM Medicines"
                                       " where med_name LIKE %(med_name)s",
                                       {'med_name': '%' + med_name + '%'})


def add_medicine_by_name_manufacturer_brand_spec_amount_default_price(med_name, med_manufacturer, brand, spec,
                                                                      amount, price):
    sql_helper.exec_sql('INSERT INTO Medicines values (%(med_name)s, %(med_manufacturer)s,%(brand)s, %(spec)s, '
                        '%(amount)s, %(price)s)',
                        {'med_name': med_name, 'med_manufacturer': med_manufacturer, 'brand': brand, 'spec': spec,
                         'amount':amount, 'price': price})

    return sql_helper.fetchall_to_dict("SELECT * FROM Medicines "
                                       "WHERE med_name = %(med_name)s, med_manufacturer = %(med_manufacturer)s, "
                                       "brand = %(brand)s, spec = %(spec)s",
                                       {'med_name': med_name, 'med_manufacturer': med_manufacturer,
                                        'brand': brand, 'spec': spec})
