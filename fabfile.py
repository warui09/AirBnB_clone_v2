#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""

import datetime
import os
import tarfile
from invoke import task

output_folder = 'versions'
output_filename = f"{output_folder}/web_static_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
source_dir = 'web_static'
hosts = ['174.129.55.61', '100.26.175.71']

@task
def do_pack(c):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with tarfile.open(output_filename, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    return output_filename
