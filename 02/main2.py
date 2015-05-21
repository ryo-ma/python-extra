# -*- coding: utf-8 -*-
import io, sys, yaml
import rest_api as rest
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == '__main__':
    argvs = sys.argv
    # コマンドライン引数が正しいか
    if len(argvs) < 2:
        print('引数が足りません')
        sys.exit(0)

    # apiキー
    api_key = ''
    # secret.ymlからapi_keyを取得
    with open('../secret.yml', mode='r', encoding='utf-8') as f:
        api_key = yaml.load(f)['api_key']
    # RestaurantAPIFactory init引数 keyword, api_key
    restaurant_api_factory = rest.RestaurantAPIFactory(argvs[1], '4487147db66b5f3496f5997e18520417')
    restaurant_api = restaurant_api_factory.create()

    for x in restaurant_api.names():
        print(x)
