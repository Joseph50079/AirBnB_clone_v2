#!/usr/bin/python3

"""A fabric file that archive and send's it to remote server"""

from fabric.api import *
import datetime


def do_pack():
    """
        Archive all web_static content with fabric api

    """
    now = datetime.datetime.now()
    current = now.strftime("%Y%m%d%H%M%S")
    file = "web_static_{}.tgz".format(current)
    local('mkdir -p versions')
    correct = local('tar -czvf versions/{}".tgz web_static'.format(file))
    if correct is not None:
        return file
    else:
        return None
