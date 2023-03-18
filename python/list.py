#list
def fun(s):
    n_l=0
    f_r=[]
    n_d=0
    c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    d=['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(s)):
        if(s[i] in c):
            n_l+=1
    for j in range(len(s)):
        if s[j] in d:
            n_d+=1
    f_r.append(n_l)
    f_r.append(n_d)
    print(f_r)
fun("Ayus 123")
