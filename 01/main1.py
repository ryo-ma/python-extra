# -*- coding: utf-8 -*-
import io, sys, requests, yaml
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if __name__ == '__main__':
    argvs = sys.argv
    # apiキー
    api_key = ''
    # secret.ymlからapi_keyを取得
    with open('../secret.yml',mode='r', encoding='utf-8') as f:
        api_key = yaml.load(f)['api_key']
    url = 'http://api.gnavi.co.jp/ver1/RestSearchAPI/?keyid=' + api_key + '&format=json&name=' + argvs[1]
    re = requests.get(url)

    # 検索結果がない場合のエラー処理
    if 'rest' not in re.json():
        raise KeyError('該当しませんでした')

    for x in re.json()['rest']:
        print(x['name'])
