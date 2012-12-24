#!/bin/bash
LOG = /usr/lib/cgi-bin/test_log
cp -T test.py /usr/lib/cgi-bin/test
if [ ! -d $LOG ] ; then mkdir $LOG ; fi
chmod 777 $LOG
cp -r test_questions /usr/lib/cgi-bin
cp -r test_images /var/www

