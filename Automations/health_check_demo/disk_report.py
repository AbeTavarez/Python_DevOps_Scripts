#!/usr/bin/env python3
import shutil

du = shutil.disk_usage("/")

# Disk Space
print("Your Total Space ->", du)

# * Calculate amount of free disk space percentage
print("Free Disk Space % :", du.free / du.total * 100)
