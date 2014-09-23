# coding: utf-8

import time
import smtplib
from email.mime.text import MIMEText

from model import ArticleModel, Session

import config


def send_mail(subject, content, toname, toemail):
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = "%s<%s>" % (config.SMTP_USERNAME, config.SMTP_USER)
    msg['To'] = "%s<%s>" % (toname, toemail)
    msg['Subject'] = subject

    s = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
    s.login(config.SMTP_USER, config.SMTP_PASSWORD)
    s.sendmail(config.SMTP_USER, [toemail], msg.as_string())
    s.quit()


def cron():
    gt = (round(time.time()/86400) - config.NOTICE_PERIOD) * 86400
    lt = gt + 86400
    article_list = Session.query(ArticleModel).filter(lt <= ArticleModel.posttime, ArticleModel.posttime < gt).all()
    if article_list:
        names = "\n".join([article.title for article in article_list])
        subject = u"文章到期提醒"
        content = (u"以下%d篇文章已经到期\n%s" % (len(article_list), names)).replace('\n','<br />\n')
        send_mail(subject, content, config.NOTICE_NAME, config.NOTICE_MAIL)
    else:
        print "no articles to be notify"


if __name__ == "__main__":
    cron()
