#!/usr/bin/python3

"""A fabric file that archive and send's it to remote server"""

from fabric import task

@task
def do_pack():
    local('tar -czvf versions/web_static_"$(date +"%Y%m%d%H%M%S")".tgz web_static')
