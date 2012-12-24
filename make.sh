#!/usr/bin/bash
chmod +x test.py
cp -T test.py /usr/lib/cgi-bin/test
cp -r test_questions /usr/lib/cgi-bin
cp -r test_images /var/www

