#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime
import os


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
