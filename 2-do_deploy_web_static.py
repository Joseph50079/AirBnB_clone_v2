#!/usr/bin/env python3

"""Module for deloying local files to the server using Fabric API"""
import os
from fabric.api import *


def do_pack():
    """
     Archive all web_static content with fabric api

    """
    now = datetime.datetime.now()
    current = now.strftime("%Y%m%d%H%M%S")
    file = "web_static_{}.tgz".format(current)
    local('mkdir -p versions')
    correct = local("tar -czvf versions/{} web_static".format(file))
    if correct is not None:
        return "versions/{}".format(file)
    else:
        return None


def do_deploy(archive_path):
    env.hosts = ['52.201.156.75', '54.172.255.78']
    env.user = 'ubuntu'
    if os.path.exists(archive_path):
        return False
    else:
        put(archive_path, remote='/tmp/')
        web_dir = archive_path.split('/')[1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(web_dir))
        run('tar -xvzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_path, web_dir))
        run('rm -rf /tmp/{}'.format(archive_path))
        run('rm -rf /data/web_static/current')
        run('ln -sF /data/web_static/releases/{} /data/web_static/current')
        return True
