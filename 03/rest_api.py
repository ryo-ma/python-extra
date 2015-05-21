# -*- coding: utf-8 -*-
import requests, re

# Factoryパターン用クラス
class RestaurantAPIFactory:
    def __init__(self, keyword, api_key,  prefecture_code):
        self.keyword = keyword
        self.api_key = api_key
        self.prefecture_code = prefecture_code

    # 引数のキーワードの言語によってRestaurantAPIオブジェクトを返却
    def create(self):
        if(re.compile(r'[ぁ-ん]|[ァ-ン]|[一-龥]|[０-９]]').match(self.keyword)):
            print("Normal create")
            return NormalRestaurantAPI(self.keyword, self.api_key,  self.prefecture_code)
        else:
            print("Multi create")
            return MultilingualRestaurantAPI(self.keyword, self.api_key,  self.prefecture_code)

class RestaurantAPI:
    def __init__(self, url):
        self.url = url
        self.requests = None

    # request結果をjsonとして返却
    def json(self):
        if self.requests is None:
            self.requests = requests.get(self.url)
        return self.requests.json()


class NormalRestaurantAPI(RestaurantAPI):
    def __init__(self, keyword, api_key,  prefecture_code):
        url = 'http://api.gnavi.co.jp/ver1/RestSearchAPI/?keyid=' + api_key \
              + '&format=json&name=' + keyword \
              + '&pref=' + prefecture_code
        RestaurantAPI.__init__(self, url)

    # request結果のnameをnameリストとして返却
    def names(self):
        if self.requests is None:
            self.requests = requests.get(self.url)

        # 検索結果がない場合のエラー処理
        if 'rest' not in self.requests.json():
            raise KeyError('該当しませんでした')
        return [x['name'] for x in self.requests.json()['rest']]

class MultilingualRestaurantAPI(RestaurantAPI):
    def __init__(self, keyword, api_key,  prefecture_code):
        url = 'http://api.gnavi.co.jp/ver2/RestSearchAPI/?keyid=' + api_key \
              + '&format=json&name=' \
              + keyword \
              + '&pref=' + prefecture_code

        RestaurantAPI.__init__(self, url)

    # request結果のnameをnameリストとして返却
    def names(self):
        if self.requests is None:
            self.requests = requests.get(self.url)

        # 検索結果がない場合のエラー処理
        if 'rest' not in self.requests.json():
            raise KeyError('該当しませんでした')
        return [x['name']['name'] for x in self.requests.json()['rest']]