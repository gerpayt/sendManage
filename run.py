import web
from controller import ArticleController
from model import ArticleModel


render = web.template.render('template') 

urls = (
    '/', 'index',
    '/article', 'ArticleController',
    '/article/(.*)', 'ArticleController'
)


class index:
    def GET(self):
        return render.index()

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

application = app.wsgifunc()
