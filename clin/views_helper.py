import random

from django.contrib import auth
from django.http import HttpResponse

from clin.responses import success_json_response
from . import sql_helper


def login_root(request):
    user = auth.authenticate(username="root", password="root")
    if user is not None:
        auth.login(request, user)
    return success_json_response({'user': {'username': user.uname}})


def add_user(request):
    sql = 'insert into Users values (%(username)s, %(password)s, %(name)s, %(email)s)'
    for i in range(20):
        data={}
        data['username'] = 'A' + str(i)
        data['name'] = 'A' + str(i)
        data['email'] = 'A' + str(i) + '@test.com'
        data['password'] = 'root'
        sql_helper.exec_sql(sql, data)

    return HttpResponse('Users added', status=200)
