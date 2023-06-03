import utilities as ut

import math

def brutal_dynamic(v,w,s,n_items,max_weight):
    
    f=[0]*(max_weight+1)
    print(f)
    for i in range(0, n_items):
        for j in range(max_weight,w[i]-1,-1):
            for k in range(0, min(s[i], j//w[i])):            
                f[j] = max(f[j], f[j-k*w[i]]+k*v[i])
    return f

def bit_optime_dynamic(v_in,w_in,s_in,n_items,max_weight):
    index = 0
    length= 0
    for s in s_in:
        length+=s
  
    v=[0]*(length+1)
    w=[0]*(length+1)
    f=[0]*(max_weight+1)
    # 二进制优化 成为 01 背包
    for i in range(0,n_items):
        c = 1
        p, h, k = w_in[i],v_in[i],s_in[i]
        while k > c:
            k -= c
            w[index] = c * p
            index += 1
            v[index] = c * h
            c *= 2
        w[index] = p * k
        index += 1
        v[index] = h * k
    # 01背包
    for i in range(1, length + 1):
        for l in range(max_weight, w[i] - 1, -1):
            f[l] = max(f[l], f[l - w[i]] + v[i])

    return f

data_path="TestDatasetMuti"
filenames=ut.getListofFiles(data_path)

for filename in filenames:
    # print(filename)
    data=ut.readfile_from_3(data_path+"/"+filename)
    print(data_path+"/"+filename)

    N=data[0][0]
    C=data[0][1]
    v=[]
    w=[]
    s=[]
    for row in data[1:]:
        v.append(row[0])
        w.append(row[1])
        s.append(row[2])
    print(v)
    print(w)
    print(s)
    # print(data)
    # ans=brutal_dynamic(v,w,s,N,C)
    # print(ans)

    ans2=bit_optime_dynamic(v,w,s,N,C)
    print(ans2)

    






