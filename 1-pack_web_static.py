#!/usr/bin/python3

"""A fabric file that archive and send's it to remote server"""

from fabric.api import *


def do_pack():
    local('mkdir versions')
    return local('tar -czvf versions/web_static_"$(date +"%Y%m%d%H%M%S")".tgz web_static')
