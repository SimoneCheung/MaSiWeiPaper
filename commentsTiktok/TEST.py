import re
pattern = re.compile(r'\d+')

liebiao=[]
#filepath = 'data.txt'
#with open(filepath, encoding='utf-8') as fp:
   #line = fp.readline()
   #cnt = 1
   #while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       #line = fp.readline()
       #cnt += 1
       #print(re.match('展开'+r'\d+'+'条回复',line))
   #print (line)


f = open ('data.txt','r',encoding='utf-8') # This file is to store all the links of songs, such as "/cny216829x11x1.htm"
lines = f.readlines() # Read all the lines from the file
for line in lines:
    line1=line.strip()
    #print(re.match('展开'+r'\d+'+'条回复',line1))
    zhankai=re.match('展开'+r'\d+'+'条回复',line1)
    if zhankai != None:
        liebiao= liebiao + [zhankai]
f.close()
print (liebiao)