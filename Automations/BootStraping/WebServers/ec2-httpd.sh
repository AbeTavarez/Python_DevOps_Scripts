#!/bin/bash

#==========================================
# INSTALL APACHE SERVER ON AMAZON LINUX 2
#==========================================

# Get super user priviliges
sudo su

#=== Update and Install httpd (Linux 2 Version) ===

# Updates instance (server)
yum update -y 
# Install httpd.x86_64
yum install -y httpd.x86_64
# Start httpd service
systemctl start httpd.service
# Enables httpd service auto-restart if instance gets re-started
systemctl enable http.service
# -OPTIONAL: Overwrites apache welcome index.html file with instance name
echo "Welcome $(hostname -f) is now running..." > /var/www/html/index.html 