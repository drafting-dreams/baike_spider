# -*- coding: utf-8 -*-
from urllib import request


class Downloader(object):
    def download(self, url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            print("get code is not 200")
            return None

        #print(response.read())
        return response.read()
