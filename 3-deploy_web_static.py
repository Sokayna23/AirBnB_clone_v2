#!/usr/bin/python3
""" Fabric script that distributes an archive to web servers """
from fabric.api import *
from os.path import exists
from os import makedirs
from datetime import datetime

env.hosts = ['18.210.14.153', '34.229.69.147']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


@task
def do_pack():
    """ generates a .tgz archive from the content of web_static folder """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
                now.year, now.month, now.day, now.hour, now.minute, now.second
                )
        archive_path = "versions/{}".format(archive_name)
        local("tar -cvaf {} web_static".format(archive_path))
        return (archive_path)

    except Exception as e:
        return None


@task
def do_deploy(archive_path):
    """ do_deploy function """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        filename = archive_path.split('/')[-1]
        folder = "/data/web_static/releases/{}".format(filename.split('.')[0])
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


@task
def deploy():
    """
    Call the do_pack() function and store the path of the created archive.
    Return False if no archive has been created.
    Call the do_deploy(archive_path) function, using the new path of
    the new archive.
    Return the return value of do_deploy.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()
