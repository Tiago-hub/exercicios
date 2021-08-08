import os
import subprocess

def bs(ls):
    i=0
    while i<len(ls):
        j=0
        while j<len(ls):
            if int(ls[i][0])>=int(ls[j][0]):
                temp = ls[i]
                ls[i] = ls[j]
                ls[j] = temp
            j = j+1
        i=i+1
output = subprocess.check_output(['ps','-e','|','grep',os.environ['USER']],shell=True,universal_newlines=True).strip().split('\n')
a = []
j=1
while j<len(output):
    i=output[j]
    i = i.split()
    a.append(i)
    j=j+1
bs(a)
i=output[0]
i = i.split()
a.insert(0,i)
j=0
while j<len(output):
    if(j<3):
        print('\t'.join(a[j]))
    j=j+1