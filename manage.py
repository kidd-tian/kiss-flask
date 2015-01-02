# -*- coding: utf-8 -*-

from flask.ext.script import Manager, prompt_bool

from app import app
from app.extensions import db
from app.index import Home

manager = Manager(app)


@manager.command
def hello():
    """print hello world"""
    print 'hello, world'


@manager.command
def drop():
    """drop database tables"""
    if prompt_bool("Are you sure to drop all tables?"):
        db.drop_all()


@manager.command
def create():
    """create tables from sqlalchemy models"""
    db.create_all()
    idx = Home(
        name=u'baijian',
    )
    db.session.add(idx)
    db.session.commit()


@manager.command
def recreate():
    """init/reset database"""
    if prompt_bool("Are you sure to drop all db if you have init db before:"):
        drop()
        create()


@manager.command
def run():
    """Run local server"""
    app.run(host='0.0.0.0', port=8081, debug=True)


if __name__ == '__main__':
    manager.run()