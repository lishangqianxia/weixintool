from django.shortcuts import render

# Create your views here.

from django.views import View

from django.http import JsonResponse
from utils.response import wrap_json_response, ReturnCode, CommonResponseMixin
from utils.auth import c2s
import json
from .models import User


def test_session(request):
    request.session['message'] = 'Test Django Session OK!'
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    print(response)
    return JsonResponse(data=response, safe=False)


def test_session2(request):
    print('session content: ', request.session.items())
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)


class UserView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        pass


def __authorize_by_code(request):
    #  使用wx.login的到的临时code到微信提供的code2session接口授权
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    code = post_data.get('code').strip()
    app_id = post_data.get('appId').strip()
    nickname = post_data.get('nickname').strip()

    response = {}
    if not code or not app_id:
        response['message'] = 'authorized failed, need entire authorization data.'
        response['code '] = ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=response, safe=False)

    data = c2s(app_id, code)
    openid = data.get('openid')
    print('get openid: ', openid)
    if not openid:
        response = wrap_json_response(code=ReturnCode.FAILED, message='auth failed')
        return JsonResponse(data=response, safe=False)

    request.session['open_id'] = openid
    request.session['is_authorized'] = True

    if not User.objects.filter(open_id=openid):
        new_user = User(open_id=openid, nickname=nickname)
        print('new user: open_id: %s, nickname: %s' % (openid, nickname))
        new_user.save()

    response = wrap_json_response(code=ReturnCode.SUCCESS, message='auth success.')
    return JsonResponse(data=response, safe=False)
    pass