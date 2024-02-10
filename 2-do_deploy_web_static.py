#!/usr/bin/python3
""" Fabric script that distributes an archive to web servers """
from fabric.api import put, run, env
from os.path import exists
from os import makedirs


env.hosts = ['18.210.14.153', '34.229.69.147']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """ do_deploy function """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        filename = archive_path.split('/')[-1]
        folder = "data/web_static/releases/{}".format(filename.split('.')[0])
        run("mkdir -p {}".format(folder))

        run("tar -xzf /tmp/{} -C {}".format(filename, folder))

        run('mv {}/web_static/* {}/'.format(folder, folder))

        run('rm -rf {}/web_static'.format(folder))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(folder))

        print("New version deployed!")

        return True
    except Exception as e:
        return False
