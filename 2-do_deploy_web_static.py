#!/usr/bin/python3
"""
Distributes an archive to web servers using Fabric
"""

from fabric.api import *
from os.path import exists
from datetime import datetime

env.user = sys.argv[5]
env.hosts = [54.237.60.175, 100.26.175.71]


def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract archive to /data/web_static/releases/<archive filename without extension>
        archive_filename = archive_path.split("/")[-1]
        folder_name = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/{}".format(folder_name)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")

        return True
    except Exception as e:
        print("Error deploying: {}".format(e))
        return False
