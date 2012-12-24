#!/usr/bin/python
#from operator import methodcaller
#b = map(methodcaller("split", "|"), a)
from random import randrange
from os.path import exists
import cgi
import cgitb
#cgitb.enable(display=0, logdir="/var/log/cgi")
qdir = './test_questions/'
def getexistence(n):
	return exists(qdir+str(n)+'.txt')
def getanswer(n,i):
	f = filter(lambda x: '|' in x,open(qdir+str(n)+'.txt','r').read().split('\n'))[i].split('|')
	return int(f[len(f)-1])
def getquestion(n):
	f = filter (lambda x: '|' in x,open(qdir+str(n)+'.txt','r').read().split('\n'))
	i = randrange(len(f))
	return f[i].split('|')[:-1],i
		
cgitb.enable(display=0, logdir="/var/log/cgi_test")
form = cgi.FieldStorage()

print "Content-Type: text/html"
print
print "<!doctype html>"
print "<html>"
print "\t<head>"
print '\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>'
print "\t\t<title>Test</title>"
print "\t</head>"
print "\t<body>"
if form.getvalue('submit'):
	k = 0
	n = 1
	while getexistence(n):
		if form.getvalue(str(n)):
			ans = form.getvalue(str(n)).split(';')
			if getanswer(n,int(ans[0])) == int(ans[1]):
				k+=1
			#else:
			#	print(str(n))
		n+=1
	print "\t\t<h1> Result is "+str(k)+"/"+str(n-1)+" &#8212; "+str(100*k/float(n-1))+"% </h1>"
else:
	n = 1
	print '\t\t<form action="/cgi-bin/test" method="POST">'
	while getexistence(n):
		f,i = getquestion(n)
		print "\t\t\t<p>"
		print "\t\t\t\t"+str(n)+". "+f[0]+" <br/>"
		for t in range(1,len(f)):
			print '\t\t\t\t<input type="radio" name="'+str(n)+'" value="'+str(i)+';'+str(t)+'"/> '+f[t]+" <br/>"
		print "\t\t\t</p>"
		n+=1
	print '\t\t\t<input type="submit" name="submit" value="check!"/>'
	print '\t\t</form>'
print "\t</body>"
print "</html>"
