import rsa
import base64

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rsa import DecryptionError

from clin.forms import LoginForm
from clin.responses import success_json_response, error_json_response
from clin.managers import doctor_manager


@csrf_exempt
def login(request):
    print(request)
    print(request.user)
    if request.user.is_authenticated:
        user = request.user
        doctors = doctor_manager.get_doctors_by_uname(user.uname)
        is_doctor = len(doctors) > 0
        is_admin = is_doctor
        return success_json_response({'user': {'username': request.user.uname,
                                               'name': request.user.name,
                                               'isAdmin': is_admin,
                                               'isDoctor': is_doctor}})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            private_key = rsa.PrivateKey.load_pkcs1(('-----BEGIN RSA PRIVATE KEY-----\n \
                MIICXAIBAAKBgQClKNC9Gyk0K2d3x1XnJhsNQOm4pqem0UmElIH6rvUSHmbx9R1S\n \
                HZSLqE7biTcYhkU8gYe0+fIBeExt/qW4L6IbEB3XG/Xv0rarK18vCNulkD43eDae\n \
                JZPOIdy3nItXiBIpNQxEu8MiOtqTIPeGIcueIOP0C3+HeIZFiKPSZMoteQIDAQAB\n \
                AoGBAIQQyCF/N4p87qar4bgNE3Kcpoe906+kCOqYKft/rX4Ii38M5p5EAwVN14jb\n \
                BxB4RaLlXNPNTcP5IvyNtIw8op1CZJZxdneTKjquH+cBYdZE5v/UpQfa1PP3o22b\n \
                0/jGtHyCGJzzZ/+DlCtgTBLJsK7e5mJPw8X9hvqR+kIPDoXRAkEA01CL26Ufr0PC\n \
                /gGMpOvI6iK8DDwBdE8ISrW+XkgixSnPBZcYrhKnLi3zvOg5yEMEBCqt9Wi/qorW\n \
                h4ZBqzVbVQJBAMgVq936/15lwJeSv6Z7Ssm7iVsLETr7xFt9m8CT3+FykrtNBZQx\n \
                rOm/daLfyTjXNsv0EaePVF6xCfyuQ7698ZUCQBeqsb9L4xySDki8i6/86GewtDb6\n \
                kX8hSuBzMnsEwUAryo/puE3msOqvItlJeQ9A0jZVQV52+OB05EoRc1FljHECQCDT\n \
                bV79zuetyesUKF0n3R07p01Ig4spww0/jk4J9LEIGwqfmEq326Z9ws716A1rQZI0\n \
                eLEE0tK2OO07qeGhSAECQEXbD/vOhPYzpME56uyev9hNBm61k4Uc4JDpq6yz81OB\n \
                +NMBbLi1tT4RBVxJKPD38CFKR0umqzVRygAl8PuOECY=\n \
                -----END RSA PRIVATE KEY-----').encode())

            try:
                password = rsa.decrypt(base64.b64decode(password), private_key)
            except DecryptionError:
                return error_json_response('密码错误，请重试。Wrong password. Please try again.')

            user = auth.authenticate(username=username, password=password)

            if user is not None:  # and user.is_active:
                auth.login(request, user)
                doctor = doctor_manager.get_doctors_by_uname(user.uname)
                is_doctor = len(doctor) > 0
                is_admin = is_doctor
                return success_json_response({'user': {'username': request.user.uname,
                                                       'name': request.user.name,
                                                       'isAdmin': is_admin,
                                                       'isDoctor': is_doctor}})
            else:
                return error_json_response('密码错误，请重试。Wrong password. Please try again.')
        else:
            return error_json_response('用户不存在，请检查用户名。Invalid username')

    return error_json_response('未登录，请登录后使用。User not logged in.')


@csrf_exempt
def logout(request):
    auth.logout(request)
    return success_json_response({'message': '注销成功。Successfully log out'})


@csrf_exempt
def reject(request):
    return error_json_response('未登录。User not logged in.')


@csrf_exempt
def default(request):
    return error_json_response('API不存在。No such API')
