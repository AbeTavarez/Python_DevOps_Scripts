#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
cd /var/www/html
EC2AZ=$(curl -s http://169.254.169.254/latest/meta-data/hostname)
echo "This instance is named #EC2AZ" > index.html