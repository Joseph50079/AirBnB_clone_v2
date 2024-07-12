#!/usr/bin/python3

"""A fabric file that archive and send's it to remote server"""

from fabric.api import *
from datetime import datetime.now


def do_pack():
    now = now.strftime("%Y%m%d%H%M%S")
    file = web_static_f"{now}".tgz
    local('mkdir -p versions')
    correct = local('tar -czvf versions/{}".tgz web_static'.format(file))
    if correct is not None:
        return file
    else:
        return None
