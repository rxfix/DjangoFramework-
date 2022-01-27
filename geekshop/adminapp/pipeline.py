import requests
from django.utils import timezone


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2'
        return

    api_url = urlunparse(('https,'
                          'api.vk.com',
                          '/metod/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                            access_token=response['access_token'], v='5.131')),
                          None
                          ))
    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.about_me = data['about']


    user.save()