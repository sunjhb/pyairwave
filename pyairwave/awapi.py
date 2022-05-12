# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 9:34 AM
# @Author  : Jihu Sun
# @FileName: awapi.py
# @Software: PyCharm
from pyairwave.base import ArubaAirwavelBase
import urllib3

urllib3.disable_warnings()


class ArubaAirwave(ArubaAirwavelBase):

    def get_amp_stats(self):
        path = '/amp_stats.xml'
        resp = self.command(apiPath=path)

        return resp

    def get_folder_list(self):
        path = '/folder_list.xml'
        resp = self.command(apiPath=path)

        return resp

    def get_alert_list(self):
        path = '/alerts.xml'
        resp = self.command(apiPath=path)

        return resp

    def get_client_detail(self, client_mac):
        """
        :param client_mac: 查询终端mac地址，冒号+大写格式
        :return: 终端详情
        """

        path = '/client_detail.xml'
        apiParams = {
            'mac': client_mac
        }

        resp = self.command(apiPath=path, apiParams=apiParams)

        return resp

    def get_ap_detail(self):
        path = '/ap_detail.xml'
        resp = self.command(apiPath=path)

        return resp

    def get_amp_bssid_list(self):
        path = '/api/ap_bssid_list.xml'
        resp = self.command(apiPath=path)

        return resp

    def get_user_info(self):
        path = '/user_info.xml'
        resp = self.command(apiPath=path)

        return resp
