#!/usr/bin/python3
""" Fabric script that distributes an archive to web servers """
from fabric.api import put, run, env
from os.path import exists
from os import makedirs


env.hosts = ['18.210.14.153', '34.229.69.147']
def do_deploy(archive_path):
    """ do_deploy function """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        filename = archive_path.split('/')[-1]
        folder_name = "data/web_static/releases/{}".format(filename.split('.')[0])
        
        run("mkdir -p {}".format(folder_name))

        run("tar -xzf /tmp/{} -C {}".format(filename, folder_name))

        run("rm /tmp/{}".format(filename))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")

        return True
    except Exception as e:
        return False
