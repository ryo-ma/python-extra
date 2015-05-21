# -*- coding: utf-8 -*-
import io, sys, yaml
import rest_api as rest
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == '__main__':
    argvs = sys.argv
    # コマンドライン引数が正しいか
    if len(argvs) < 3:
        raise ValueError('引数が正しくありません')
        # apiキー
    api_key = ''
    # secret.ymlからapi_keyを取得
    with open('../secret.yml', mode='r', encoding='utf-8') as f:
        api_key = yaml.load(f)['api_key']
    # RestaurantAPIFactory init引数 keyword, api_key, 県コード
    restaurant_api_factory = rest.RestaurantAPIFactory(argvs[1], api_key, argvs[2])
    restaurant = restaurant_api_factory.create()
    for x in restaurant.names():
        print(x)
