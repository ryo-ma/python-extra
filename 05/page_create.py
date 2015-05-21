# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='cp932')

# タグをラッピングしてくれるUtilクラス
class HTMLGenerator:
    @classmethod
    def wrap_html(cls, html):
        return """<html>""" + html + """</html>"""

    @classmethod
    def wrap_title(cls, title):
        return """<title>""" + title + """</title>"""

    @classmethod
    def wrap_head(cls, head):
        return """<head>""" + head + """</head>"""

    @classmethod
    def wrap_body(cls, body):
        return """<body>""" + body + """</body>"""

    @classmethod
    def wrap_div(cls, div):
        return """<div>""" + div + """</div>"""

    @classmethod
    def wrap_link(cls, link):
        return """<a href=\"""" + link[1] + """\">""" + link[0] + """</a>"""

    @classmethod
    def wrap_image(cls, image_url):
        return """<img src=\"""" + image_url + """\" alt=\"shop_image\">"""

# Builderパターン用クラス
class PageCreator:
    def __init__(self, title):
        self.title = title
        self.text_list = []
        self.link_list = []
        self.image_list = []
        self.json_html = []

    # 文章を追加
    def add_text(self, text):
        self.text_list.append(text)

    # リンクを追加　引数:リンク名、url
    def add_link(self, link_name, url):
        self.link_list.append((link_name, url))

    # 画像を追加
    def add_image(self, image):
        self.image_list.append(image)

    # ページを生成
    def create(self):
        file_name = './index.html'
        with open(file_name, mode='w', encoding='utf-8') as f:
            f.write(self._generate_html())

    # jsonをパースして自身に追加する
    def add_json(self, json, index):
        # 検索結果がない場合のエラー処理
        if 'response' not in json:
            raise KeyError('該当しませんでした')
        for x in range(1, index + 1):
            html = ''
            html += HTMLGenerator.wrap_image(json['response'][str(x)]['photo']['image_url']['url_1024']) + '</br>'
            html += HTMLGenerator.wrap_link((json['response'][str(x)]['photo']['shop_name'],
                                             json['response'][str(x)]['photo']['shop_url'])) + '</br>'
            html += HTMLGenerator.wrap_div(json['response'][str(x)]['photo']['comment']) + '</br>'
            self.json_html.append(html)

    # HTMLGeneratorを使ってhtmlを構成し返却する
    def _generate_html(self):
        title_tag = HTMLGenerator.wrap_title(self.title)
        body = []
        # 追加されたデータをbodyに追加
        for image, link, text in zip(self.image_list, self.link_list, self.text_list):
            body.append("</br>".join([HTMLGenerator.wrap_image(image),
                                      HTMLGenerator.wrap_link(link),
                                      HTMLGenerator.wrap_div(text)]))
        # json_addされたデータをbodyに追加
        for x in self.json_html:
            body.append("</br>" + x)
        # metaタグを定義
        meta_char = """<meta content=\"text/html\" charset=\"UTF-8\"> """
        # それぞれをhead body htmlタグにラッピングする
        head_tag = HTMLGenerator.wrap_head(meta_char + title_tag)
        body_tag = HTMLGenerator.wrap_body('</br>'.join(body))
        html_tag = HTMLGenerator.wrap_html(head_tag + body_tag)
        return html_tag
