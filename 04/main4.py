# -*- coding: utf-8 -*-
import io, sys, requests, asyncio, yaml
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# タスク生成用関数
def generate_param_list(key_word, hit):
    return [request_parallel(key_word, x) for x in range(1, hit + 1)]

# コルーチン用関数
@asyncio.coroutine
def request_parallel(key_word, offset):
    # apiキー
    api_key = ''
    # secret.ymlからapi_keyを取得
    with open('../secret.yml',mode='r', encoding='utf-8') as f:
        api_key = yaml.load(f)['api_key']
    # url構成
    url = 'http://api.gnavi.co.jp/ouen/ver1/PhotoSearch/?keyid=' + api_key + \
          '&format=json&shop_name=' + key_word + \
          "&hit_per_page=1&offset_page=" + str(offset)
    re_json = requests.get(url).json()

    # 検索結果がない場合のエラー処理
    if 'response' not in re_json:
        print('該当しませんでした')
        raise
    # 店舗名/コメントで出力
    print(re_json['response']['0']['photo']['shop_name'], '/', re_json['response']['0']['photo']['comment'])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # generate_param_listのinit引数 keywordと検索件数
    loop.run_until_complete(asyncio.wait(generate_param_list("aa", 3)))
    loop.close()
