import datetime, time
import json

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine('sqlite:///' + config.DBFILE, connect_args={'check_same_thread': False}, echo=config.DEBUG)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
SessionMaker = sessionmaker()
SessionMaker.configure(bind=engine)
Session = SessionMaker()


class ArticleModel(Base):
    __tablename__ = 'article'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    code = Column(String)
    title = Column(String)
    posttime = Column(DateTime)
    remark = Column(String)

    def __init__(self, id, code, title, posttime, remark):
        self.id = id
        self.code = code
        self.title = title
        self.posttime = posttime
        self.remark = remark

    def __repr__(self):
        return json.dumps({'id': self.id, 'code': self.code, 'title': self.title, 'posttime': time.strftime('%Y-%m-%d', self.posttime.timetuple()), 'remark': self.remark})


metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
    article = ArticleModel(None, 'code', 'title', datetime.date(2014, 8, 1), 'remark')
    Session.add(article)
    article = ArticleModel(None, 'code2', 'title2', datetime.date(2014, 8, 2), 'remark2')
    Session.add(article)
    Session.commit()
