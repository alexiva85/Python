import re
import pprint

def read_file (filename):
    with open(filename) as f:
        return f.read()


pattern = r'([\w.-]+)\s-\s\d{8,10}\s\w{3,5}\s[\w./?,-]+\s(\d{2,4})\s\d+'

host_list = {}
response_list = {}

x = re.findall(pattern,read_file('nasa_19950801.tsv'))

for el in x:
    if el[0] in host_list.keys():
        host_list[el[0]]+=1
    else:
        host_list[el[0]]=1
    if el[1] in response_list.keys():
        response_list[el[1]]+=1
    else:
        response_list[el[1]]=1

pprint.pprint((sorted(host_list.items(), key=lambda x: x[1], reverse=True))[:10])
for i in response_list.keys():
    print ('Response code {} received {} times'.format(i,response_list[i]) )
