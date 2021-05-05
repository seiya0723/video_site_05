from django import template

register = template.Library()

@register.simple_tag()
def url_replace(request, field, value):
    dict_           = request.GET.copy()
    dict_[field]    = value
    return dict_.urlencode()

"""
1、リクエストオブジェクト(request)、クエリストリングの名前(page)、ページ番号を引数として関数実行
2、リクエストをコピー、pageにページ番号を当てる
3、リクエストのクエリストリングのみを返す(既存のクエリストリングにpageを追加して、全クエリストリングを返却している)
   例1: ?page=3
   例2: ?search=hoge&page=2
"""

