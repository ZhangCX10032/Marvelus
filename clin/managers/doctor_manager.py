from clin import sql_helper


def get_doctors_by_uname(uname):
    return sql_helper.fetchall_to_dict("SELECT u.name, u.email FROM Users u NATURAL JOIN Doctors WHERE uname = %(uname)s",
                                       {'uname': uname})
