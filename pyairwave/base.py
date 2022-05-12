# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 9:45 AM
# @Author  : Jihu Sun
# @FileName: base.py
# @Software: PyCharm
import requests


class ArubaAirwavelBase:
    def __init__(self, aw_info, ssl_verify=False):
        self.aw_info = aw_info
        self.ssl_verify = ssl_verify

        # Set token and cookie
        self.session = self.login()

    def login(self):
        path = "/LOGIN"
        url = "https://{}{}".format(self.aw_info['ip'], path)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        payload = {
            'credential_0': self.aw_info['username'],
            'credential_1': self.aw_info['password'],
            'destination': '/api',
        }
        amp_session = requests.Session()
        amp_session.post(url=url, headers=headers, data=payload, verify=self.ssl_verify)

        # print(amp_login.headers['X-BISCOTTI'])
        # print(amp_session.cookies)

        return amp_session

    def command(self, apiPath, apiParams={}):
        url = 'https://{}{}'.format(self.aw_info['ip'], apiPath)

        headers = {
            'Content-Type': 'application/xml',
        }

        response = self.session.get(url=url, headers=headers, params=apiParams, verify=False)

        return response.text
