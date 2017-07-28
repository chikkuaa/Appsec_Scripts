import re
#import urllib
import urllib2
#import jsbeautifier

pattern='[a-zA-Z0-9_:.]*\/+[a-zA-Z0-9_\/.#?=:-]{8,110}'
filter_pattern=[re.compile(p) for p in ['^\/\/[\w=.:-]*','^\/\/\w*','^\/\/\w*']]
set_global=set([])
fi=open("js.txt","r")
fo=open("JS_Output.txt","a")
request_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}

print "[+] Fetching JS from JS.txt.........\n\n"

for var in fi.readlines():
    try:
        request=urllib2.Request(var.strip(), headers=request_headers)
        response = urllib2.urlopen(request).read()
        print "\n[+] Fetching URLs from the JavaScript => " + var.strip() + "\n"
        matches=re.findall(pattern,response)
        if len(matches)!=0:
            for patter in filter_pattern:
                for ite in matches:
                    if patter.match(ite.strip()):
                        matches.remove(ite)
        
            set_file=set(matches)
	    if set_file.difference(set_global):
                fo.writelines("\n************************************************************************************************\n")
		fo.writelines("List of Probable URLs......"+"\n\n")
		fo.writelines("\n")
		for item in set_file.difference(set_global):
                    fo.write(item)
                    fo.write("\n")
		set_global=set_file.union(set_global)
		fo.writelines("\n\nJavaScript File used is => " + var.strip() + "\n\n\n")
    except Exception:
        print "\n[-] Not able to open URL=> "+var.strip()+" please check if it exists....\n"
fo.close()
fi.close()
                
print "\n\n\n************************Analysis is Completed******************************\n\n"
raw_input("press enter to exit ;)")
