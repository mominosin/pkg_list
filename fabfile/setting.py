from fabric.api import env
from fabric.decorators import task

@task
def ls(path):
    env.pyfile = 'ls'
    env.method = 'mainls'
    env.args   = path

@task
def find(path):
    env.pyfile = 'find'
    env.method = 'main'
    env.args   = path
