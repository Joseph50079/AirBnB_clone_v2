#!/usr/bin/python3

"""Module for deloying local files to the server using Fabric API"""
import os
from fabric.api import env, run, put, sudo


env.key_filename = '~/.ssh/id_rsa'
env.hosts = ['52.201.156.75', '54.172.255.78']
env.user = 'ubuntu'


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
    """
    Deploys archived file to server

    Args:
        archive_path: path to the archived file
     
    """

    if not os.path.exists(archive_path):
        return False

    try:

        put(archive_path, '/tmp/')
        archive_file = archive_path.split('/')[-1]
        web_dir = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(web_dir))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_file, web_dir))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(web_dir, web_dir))
        run('rm -rf /tmp/{}'.format(archive_file))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(web_dir))
        run('rm -rf /data/web_static/current')
        run('ln -sF /data/web_static/releases/{} /data/web_static/current'.format(web_dir))
        sudo('service nginx restart')
        return True

    except:
        return False
