import web
import json
from model import ArticleModel
from model import Session
import datetime, time

class ArticleController(object):
    def GET(self, id = None):
        if not id:
            article = Session.query(ArticleModel).all()
        else:
            article = Session.query(ArticleModel).get(id)
        return article

    def POST(self, id):
        pass

    def DELETE(self, id):
        Session.query(ArticleModel).filter(ArticleModel.id==id).delete()
        Session.commit()

    def PUT(self, id):
        data = web.data()
        item = json.loads(data)
        if id == '0':
            id = None
        code = item['code'] if ('code' in item) else 'code'
        title = item['title'] if ('title' in item) else 'title'
        try:
            posttime = datetime.datetime.strptime(item['posttime'], '%Y-%m-%d')
        except (KeyError, ValueError):
            posttime = datetime.datetime.now()
        remark = item['remark'] if ('remark' in item) else ''

        articleobj = ArticleModel(id, code, title, posttime, remark)
        articledict = {'code': code, 'title': title, 'posttime': posttime, 'remark': remark}
        if id:
            Session.query(ArticleModel).filter(ArticleModel.id==id).update(articledict)
        else:
            Session.add(articleobj)
        Session.commit()
