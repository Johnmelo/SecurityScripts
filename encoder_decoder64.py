import sys
import base64
string = ""
text = ""
if (len(sys.argv) > 2):
    op = sys.argv[1]
    text = sys.argv[2]
    if(op == '-e'):
        string = str(base64.encodestring(text))
    if(op == '-d'):
        string = str(base64.decodestring(text))
    print(string)
else:
    print ("need parameters")
