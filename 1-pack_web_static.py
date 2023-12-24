#!/usr/bin/python3
"""
Create archive from the contents of web_static
"""

from fabric import task
from fabric.api import *
from datetime import datetime
import os

@task
def do_pack():
    try:
        # Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Set the archive filename
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder into a .tgz archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path
        return os.path.join("versions", archive_name)
    except Exception as e:
        # Print an error message (you can customize this part)
        print("Error creating archive: {}".format(e))
        return None
