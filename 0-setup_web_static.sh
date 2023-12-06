#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Create relevant files
mkdir -p "/data/web_static/releases/"
mkdir -p "/data/web_static/shared/"
mkdir -p "/data/web_static/releases/test/"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# Create symlink
link_path='/data/web_static/current'
target_path='/data/web_static/releases/test/'

if [ -L "$link_path" ]; then
	# Remove symlink
	rm "$link_path"
fi

ln -s "$target_path" "$link_path"

# Change ownership of data file
sudo chown -R ubuntu:ubuntu /data/

# Install Nginx
sudo apt update
sudo apt install nginx -y
sudo service nginx start

# Nginx configuration file path
nginx_conf="/etc/nginx/sites-available/default"

# Directory to serve
serve_directory="/data/web_static/current/"

# URL path
url_path="/hbnb_static"

# Update Nginx configuration
cat <<EOF | sudo tee "$nginx_conf" > /dev/null
server {
    # ... other server configurations ...

    location $url_path {
        alias $serve_directory;
        index index.html;  # You can adjust this if needed
    }

    # ... other server configurations ...
}
EOF

# Restart Nginx
sudo service nginx restart

echo "Nginx configuration updated. Content of $serve_directory will be served at https://mydomainname.tech$url_path"
