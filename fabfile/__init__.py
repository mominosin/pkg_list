#coding: UTF-8
from fabric.api import env
from fabric.decorators import task,runs_once

import collections

import pkginfo

env.hosts = ['test1','test2']
env.user = 'ec2-user'
env.key_filename = ['~/.ssh/test.pem']
env.pkg_lists_sum = collections.defaultdict(int)
env.host_pkg_lists = {}

@task
def main():
    _get_host_pkg()

def _get_host_pkg():
    env.host_pkg_lists[env.host] = pkginfo.main()

def _count_pkg():
    for host_pkgs in env.host_pkg_lists.itervalues():
        for pkg in host_pkgs:
           env.pkg_lists_sum[pkg] += 1
@task
@runs_once
def print_result():
  _count_pkg()
  server_count = len(env.hosts)
  for k,v in env.pkg_lists_sum.iteritems():
      print 'pkg_name_version: ' + k
      print '  pkgcount(installd/all_server): ' + str(v) + '/' + str(server_count) + '\n'



#import sys
#
#import setting
#
#@task
#def search():
##    __import__('fabfile.' +env.pyfile)
#    import ls
#    print sys.modules.keys()
#
#    lists = getattr(__import__('fabfile.' + env.pyfile),env.method)()
#    for f in lists:
#        local('file %s' % f)
#
#@task
#def lsearch(path):
#    lists = local('ls -1 %s' % path,capture=True)
#    for f in lists.split('\n'):
#        local('file %s%s' % (path,f))
