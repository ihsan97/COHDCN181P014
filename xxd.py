import sys
import os.path

def xxd(file_path):
    f=open(file_path,'r')
    t=0
    while True:
        r=f.read(16)
        d=r
        if not r:
            break
        a=[]
        for c in r:
            a.append('%02x'%ord(c))
        b=[]
        for z in range(0,len(a),2):
            b.append(''.join((a[z:z+2])))
        kk=[]
        for i in d:
            ct=ord(i)
            if ct<32 or ct>127:
                kk.append('.')
            else:
                kk.append(i)
        step=('%08x'%(t*16))
        print('{0}: {1:<39} {2}'.format(step,' '.join(b),''.join(kk)))
        t=t+1


   
    sys.exit(1)
xxd(sys.argv[1])
