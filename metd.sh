#!/bin/bash

echo "This script creates the malicious email test directory "
echo "This directory will be deleted by the malicious email"
echo "Store this file in your home directory"
echo "Give it permisions: chmod 777 metd.sh"
echo "To run from home directory, type: ./metd.sh"
echo "To delete the directory manually"
echo "In home directory type:  rm -rf maliciousEmailTestDirectory"
echo " "
echo "This is a group project in Infsys6868 - Software Assurance"
echo "Mathew Kaplan"
echo "Kevin Folkl"
echo "Wes Jonas"
echo "Bryce Benjamin"
echo "Roshni Sharma"
echo "Ryan Bao"
echo "Gene Browder"

mkdir maliciousEmailTestDirectory
chmod 777 maliciousEmailTestDirectory
cd maliciousEmailTestDirectory

mkdir {1..10} |  touch {1..10}/{a..f}.txt 

#find ./{1..25} -type d -exec chmod 777 {} 
chmod 777 $(find ./{1..10} )
#find ./{1..25} -type f -exec chmod 777 {} +



