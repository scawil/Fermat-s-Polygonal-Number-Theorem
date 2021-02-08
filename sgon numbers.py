#fermat conjectured that for every s>=3, any natural number can be written as a sum of s sgon numbers
#given s and x, s_gon_fermat returns a list of s sgon numbers which add to x.

def s_gon(s,n):
    return ((s-2)*(n**2)-(s-4)*n)/2

def s_gon_root(s,x):
    L=0
    R=x
    while (L<=R):
        t=int((L+R)/2)
        if (s_gon(s,t)==x):
            return t
            break
        if (s_gon(s,t)<x):
            L=t+1
        else:
            R=t-1
    return R

#fermat ngon theorem
    
def sgon_check_string(s,l):
    c=0
    if len(l)>0:
        for i in l:
            c+=s_gon(s,i)
    else:
        pass
    return c

        
def recursive_gon_fermat(i,s,x):
    result=list([])
    if (i>1):
        for j in range(s_gon_root(s,x)+2):
            if sgon_check_string(s,recursive_gon_fermat(i-1,s,x-s_gon(s,j)))==x-s_gon(s,j):
                result=recursive_gon_fermat(i-1,s,x-s_gon(s,j))
                result.append(j)
                return result
                break
            else:
                pass
    else:
        if s_gon(s,s_gon_root(s,x))==x:
            result=list([s_gon_root(s,x)])
        else:
            pass
    return list(result)

def s_gon_fermat(s,x):
    y=[]
    for i in recursive_gon_fermat(s,s,x):
        y.append(s_gon(s,i))
    return y 
