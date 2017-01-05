# /usr/bin/python
# -*- coding:utf-8 -*-
import requests, re , sys

url = ['http://md5decryption.com/']
def success():
    try:
        req = requests.get(url[0])
        statuscode = req.status_code
        print('[+] Connection is '+url[0]+' : Code ['+str(statuscode)+']')
    except requests.ConnectionError:
        print('[-] Error connecting to : ' + url[0])
        sys.exit()
    except requests.ConnectTimeout:
        print('[-] Error connecting time to : ' + url[0])
        sys.exit()

success()

def brut():
   inp = raw_input('[+] Name is file : ') # input for Python 3
   f = open(inp,'r')
   text = f.readlines()
   for lines in text:
       lines = lines.replace('\n', '')
       data = {'hash': str(lines), 'submit': 'Decrypt It!'}
       headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
       req2 = requests.post(url[0], data=data,headers=headers)
       htmltext = req2.content
       find = re.findall(r"Decrypted Text: </b>(.*?)</font>", str(htmltext))
       for line in find:
           if len(line) > 1:
               print('[+] Hash found : ' + lines + ' : ' + line)
brut()
