#!/bin/bash                                                                                                                                                            
                                                                                                                                                                       
#Description:                                                                                                                                                          
#Script automate the backup, tramsfer, and removal of a local backup file.                                                                                             
                                                                                                                                                                       
#Author: Abraham                                                                                                                                                       
#=========================================================================                                                                                             
                                                                                                                                                                       
#Current day                                                                                                                                                           
DAY="$(date+%Y%m%d)"                                                                                                                                                   
                                                                                                                                                                       
#Input to the scp command                                                                                                                                              
SAVE="labsuser@127.0.0.1:/tmp"                                                                                                                                         
                                                                                                                                                                       
#Back up file                                                                                                                                                          
BACKUP="/home/labsuser/$DAY-backup-companyA.tar.gz"                                                                                                                    
                                                                                                                                                                       
#Creates tarbal                                                                                                                                                        
sudo tar -csvpzf $BACKUP /home/labsuser/companyA                                                                                                                       
                                                                                                                                                                       
# Sends backup file to tmp directory                                                                                                                                   
scp $BACKUP $SAVE                                                                                                                                                      
                                                                                                                                                                       
#Removes backup from original location                                                                                                                                 
rm $BACKUP 