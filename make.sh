#!/bin/bash
cp -T test.py /usr/lib/cgi-bin/test
if [ ! -d /usr/lib/cgi-bin/test_log ] ; then mkdir /usr/lib/cgi-bin/test_log ; fi
cp -r test_questions /usr/lib/cgi-bin
cp -r test_images /var/www

