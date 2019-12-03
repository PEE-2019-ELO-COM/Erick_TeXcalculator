import re
import sympy as sp
from sympy import sympify


def uniC(s):
    s=s.replace(' ', '')
    s=s.replace('\\cdot','*')
    s=s.replace('.','*')
    s=s.replace('^','**')
    return s

func=sp.Function('func')
x=sp.Symbol('x')

def div(s):
    
    k=0
    pattern = re.compile("{(.*?)}")
    output = pattern.findall(s)
    if output[0][0]=='\\' :
        output[0]=output[0][1:]

    if output[1][0]=='\\' :
        output[1]=output[1][1:]
        
    if (output[0].count('x')>0):
        output[0]=sympify(output[0])
        k=k+1
    else:
        output[0]=float(output[0])
        
    if (output[1].count('x')>0):
        output[1]=sympify(output[1])
        k=k+1
    else:
        output[1]=float(output[1])
        
    out=sp.simplify(output[0]/output[1])
    if k==0:
        out = output[0]/output[1]
    return out

def mult(m):
    m=uniC(m)
    a=m[:m.find('*')]
    b=m[m.find('*')+1:]
    if (a.count('x')>0 or b.count('x')):
        out=sympify(a)*sympify(b)
    else:
        out=float(a)*float(b)
    return out

def soma(m):
    m=uniC(m)
    a=m[:m.find('+')]
    b=m[m.find('+')+1:]
    if (a.count('x')>0 or b.count('x')>0):
        out=sympify(a)+sympify(b)
    else:
        out=float(a)+float(b)
    return out

def sub(m):
    m=uniC(m)
    a=m[:m.find('-')]
    b=m[m.find('-')+1:]
    if (a.count('x')>0 or b.count('x')>0):
        out=sympify(a)-sympify(b)
    else:
        out=float(a)-float(b)
    return out


def integra(s):
    pattern = re.compile("int(.*?)dx")
    output = pattern.findall(s)
    if output[0][0]=='\\' :
        output[0]=output[0][1:]
    output[0]=uniC(output[0])
    output[0]=sp.integrate(sympify(output[0]),x)
    return output[0]

def deriv(s):
    if s.find('math')>0:
        pattern = re.compile("mathrm{d}(.*?)}")
        output = pattern.findall(s)
        if output[0][0]=='\\' :
            output[0]=output[0][1:]
        res=uniC(output[0])
        res=sp.diff(sympify(output[0]),x)
    else:
        res=0
        
    return res


def operator(s):
    s=uniC(s)
    a=''
    b=''
    c=''
    d=''
    res=0
    auxF=''
    if not (s[s.find('{')+2]=='m') and (s.find('frac')>0):
        for i in range(0,len(s)):
            if (i<s.find('\\')) or (i>s.find('}',s.find('}')+1)):
                a=a+s[i]
            else:
                b=b+s[i]
        b=div(b)
        try:
            c=s[s.find('\\')-1]
            if (c=='+' or c=='-' or c=='*'):
                auxF=s[:s.find('\\')-1]
            else:
                auxF=0
            if c=='+':
                res=res+sympify(auxF)+b
            elif c=='-':
                res=res+sympify(auxF)-b
            elif c=='*':
                res=res+sympify(auxF)*b
            else:
                res=res+b

        except:
            res=b


        try:
            d=s[s.find('}',s.find('}')+1)+1]
            if d=='+':
                res=res+sympify(s[s.find('}',s.find('}')+1)+1:])
            elif d=='-':
                res=res+sympify(s[s.find('}',s.find('}')+1)+1:])
            elif (d=='*') and (c=='*'):
                res=res*sympify(s[s.find('}',s.find('}')+1)+2:])
            elif (d=='*') and (c=='+'):
                res=(res-sympify(auxF))*sympify(s[s.find('}',s.find('}')+1)+2:])+sympify(auxF)
            elif (d=='*') and (c=='-'):
                res=(res-sympify(auxF))*sympify(s[s.find('}',s.find('}')+1)+2:])+sympify(auxF)
            else:
                res=b
        except:
            if res==0:
                res=b
                
    elif (s[s.find('{')+2]=='m') and (s.find('frac')>0):
        for i in range(0,len(s)):
            if (i<s.find('\\')) or (i>s.find('}',s.find('}')+6)):
                a=a+s[i]
            else:
                b=b+s[i]
        b=deriv(b)
        try:
            c=s[s.find('\\')-1]
            
            if (c=='+' or c=='-' or c=='*'):
                auxF=s[:s.find('\\')-1]
            else:
                auxF=0            
            if c=='+':
                res=res+sympify(auxF)+b
            elif c=='-':
                res=res+sympify(auxF)-b
            elif c=='*':
                res=res+sympify(auxF)*b
            else:
                res=res+b
        except:
            res=b
        

        try:
            d=s[s.find('}',s.find('}')+6)+1]
            if d=='+':
                res=res+sympify(s[s.find('}',s.find('}')+6)+1:])
            elif d=='-':
                res=res+sympify(s[s.find('}',s.find('}')+6)+1:])
            elif (d=='*') and (c=='*'):
                res=res*sympify(s[s.find('}',s.find('}')+6)+2:])
            elif (d=='*') and (c=='+'):
                res=(res-sympify(auxF))*sympify(s[s.find('}',s.find('}')+6)+2:])+sympify(auxF)
            elif (d=='*') and (c=='-'):
                res=(res-sympify(auxF))*sympify(s[s.find('}',s.find('}')+6)+2:])+sympify(auxF)
            else:
                res=b
        except:
            if res==0:
                res=b
 
    elif s.find('int')>0:
        for i in range(0,len(s)):
            if (i<s.find('\\')) or (i>s.find('dx')+1):
                a=a+s[i]
            else:
                b=b+s[i]
        b=integra(b)
        try:
            c=s[s.find('\\')-1]
        
            if (c=='+' or c=='-' or c=='*'):
                auxF=s[:s.find('\\')-1]
            else:
                auxF=0
            if c=='+':
                res=res+sympify(auxF)+b
            elif c=='-':
                res=res+sympify(auxF)-b
            elif c=='*':
                res=res+sympify(auxF)*b
            else:
                res=res+b
        except:
            res=b
            


        try:
            d=s[s.find('dx')+2]           
            if d=='+':
                res=res+sympify(s[s.find('dx')+3:])
            elif d=='-':
                res=res-sympify(s[s.find('dx')+3:])
            elif (d=='*') and ((c=='*') or auxF==0):
                res=res*sympify(s[s.find('dx')+3:])        
            elif (d=='*') and ((c=='+') or auxF==0):
                res=(res-sympify(auxF))*sympify(s[s.find('dx')+3:])+sympify(auxF)
            elif (d=='*') and ((c=='-') or auxF==0):
                res=(res-sympify(auxF))*sympify(s[s.find('dx')+3:])+sympify(auxF)
            else:
                res=b
        except:
            if res==0:
                res=b
    else:
        s=s.replace('\\','')
        res=sympify(s)
    
    return res


def latifa(s):
    s= str(s)
    s=s.replace('**', '^')
    s=s.replace('*','\\cdot ')
    s=s.replace('.00000000000000','')
    return s

def preview(s):
    count=0
    if s[:7]=='preview':
        pattern = re.compile(":(.*?):")
        output = pattern.findall(s)
        res=output[0]
        count=count+1
    else:
        res=s
    return res,count