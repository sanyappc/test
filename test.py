#!/usr/bin/python
#from operator import methodcaller
#b = map(methodcaller("split", "|"), a)
#from random import randrange,seed
import random
from os.path import exists,getsize
import cgi
import cgitb
import datetime

qdir = './test_questions/'
ldir = './test_log/'
lfile = ldir+'checks.log'

def getexistence(n):
	return exists(qdir+str(n)+'.txt')
def getanswer(n,i):
	f = filter(lambda x: '|' in x,open(qdir+str(n)+'.txt','r').
		read().split('\n'))[i].split('|')
	return int(f[len(f)-1])
def getquestion(n):
	random.seed()
	f = filter (lambda x: '|' in x,open(qdir+str(n)+'.txt','r').
		read().split('\n'))
	i = random.randrange(len(f))
	return f[i].split('|')[:-1],i
def gethash(i):
	return str(hash(('fefsfrrgref','hthteeees')+i+('awfcngmhfbb','ajwbfucwwa')))
		
cgitb.enable(display=0, logdir=ldir)
form = cgi.FieldStorage()

print "Content-Type: text/html\r"
print "Cache-Control: no-cache, no-store, max-age=0, must-revalidate\r"
print "Cache-Control: post-check=0, pre-check=0\r"
print "Pragma: no-cache\r"
print "Expires: Fri, 01 Jan 1990 00:00:00 GMT\r"
print "\r"
print "<!doctype html>"
print "<html>"
print "\t<head>"
print '\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>'
print "\t\t<title>Test</title>"
print "\t</head>"
print "\t<body>"
if form.getvalue('submit'):
	if form.getvalue('surname'):
		k = 0 # true
		c = 0 # checked
		n = 1
		hashtuple = ()
		while getexistence(n):
			if form.getvalue(str(n)):
				ans = form.getvalue(str(n)).split(';')
				c += 1
				hashtuple += (int(ans[0]),)
				if getanswer(n,int(ans[0])) == int(ans[1]):
					k+=1
				#I need to optimise this
			n+=1
		if c == (n-1):
			if form.getvalue('hidden') == gethash(hashtuple):
				print "\t\t<h1> Result is "+str(k)+"/"+str(n-1)+" &#8212; "+\
					str(100*k/float(n-1))+"% </h1>"
				surname = form.getvalue('surname')
				#let's log without logging and without rotation
				log = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+\
					' hash: '+gethash(hashtuple)+': surname: '+surname+\
					': result: '+str(k)+\
					'/'+str(n-1)+' - '+str(100*k/float(n-1))+'%\n'
				if exists(lfile) and (getsize(lfile) < 1024 * 1024):
					open(lfile,'a+').write(log)
				else:
					open(lfile,'w+').write(log)
			else:
				print "\t\t<h1> Wrong data </h1>"
		else:
			print "\t\t<h1> Answer to all questions is required </h1>"
	else: print "\t\t<h1> Surname is required </h1>"
else:
	n = 1
	hashtuple = ()
	print '\t\t<form action="/cgi-bin/test" method="POST" autocomplete="off">'
	while getexistence(n):
		f,i = getquestion(n)
		hashtuple += (i,)
		print "\t\t\t<p>"
		print "\t\t\t\t"+str(n)+". "+f[0]+" <br/>"
		for t in range(1,len(f)):
			print '\t\t\t\t<input type="radio" name="'+str(n)+\
				'" value="'+str(i)+';'+str(t)+'"/> '+f[t]+" <br/>"
		print "\t\t\t</p>"
		n+=1
	print "\t\t\t<p>"
	print '\t\t\t\tsurname: <input type="text" name="surname" value=""/>'
	print "\t\t\t</p>"
	print "\t\t\t<p>"
	print '\t\t\t\t<input type="hidden" name="hidden" value="'+gethash(hashtuple)+'">'
	print '\t\t\t\t<input type="hidden" id="refreshed" value="no">'
	print '\t\t\t\t<input type="submit" name="submit" value="check!"/>'
	print "\t\t\t</p>"
	print '\t\t</form>'
print "\t</body>"
print "</html>"
