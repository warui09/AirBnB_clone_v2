#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""

import datetime
import os
import tarfile
from fabric.api import *

output_folder = 'versions'
output_filename = f"{output_folder}/web_static_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
source_dir = 'web_static'
env.hosts = ['174.129.55.61', '100.26.175.71']

def do_pack():
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with tarfile.open(output_filename, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    return output_filename
