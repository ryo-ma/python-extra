# -*- coding: utf-8 -*-
import io, sys, requests, webbrowser, yaml
import page_create as page

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == '__main__':
    # apiキー
    api_key = ''
    # secret.ymlからapi_keyを取得
    with open('../secret.yml', mode='r', encoding='utf-8') as f:
        api_key = yaml.load(f)['api_key']
    # 検索キーワード
    name = 'aa'
    # 検索件数
    hit_per_page = 3
    url = 'http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/?keyid=' + api_key + \
          '&format=json&shop_name=' + name + \
          '&hit_per_page' + str(hit_per_page)
    # 接続
    re_json = requests.get(url).json()
    # PageCreatorを生成しtitleを引数に与える
    page_creator = page.PageCreator('グルメ')
    # jsonのデータをPageCreatorに渡す
    page_creator.add_json(re_json, hit_per_page)
    # pageを生成
    page_creator.create()
    # 生成したpageを開く
    webbrowser.open_new_tab('http://localhost:63342/extra/05/index.html')
