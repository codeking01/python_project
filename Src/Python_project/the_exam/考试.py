
# 第一题
def fun1(x, y, z):
    import sympy
    # hxy  918
    # ya 948
    # 输入 xyz
    a = 3 * x - 2 * y + z
    b = 2 * x - 3 * y + z
    c = x - 2 * y + 3 * z
    d = 5 * x + 2 * y - z
    print('a,b,c,d分别为', a, b, c, d)


# 第二题
# 33 23 31
# 每个人的数不一样自己按照题目的表达式输入
def fun2(a, b, c, d):
    import numpy as np
    A = np.mat([[a, b, c, 2], [b, a, 1, 6], [3, 1, 5, 8], [2, b, 3, c]])
    B = np.mat([[a, b, c, d], [b, a, 1, 6], [3, d, 5, 2], [1, a, 3, c]])
    C = np.mat([[a, d, c, 3], [b, a, 1, 6], [b, 1, a, d], [8, b, d, c]])
    print('矩阵A：', A)
    print('矩阵B：', B)
    print('矩阵C：', C)
    return A,B,C

# 第三题
def fun3(A, B, C):
    import numpy as np
    A1 = np.array(A)
    B1 = np.array(B)
    C1 = np.array(C)
    print('数组A1：', A1)
    print('数组B1：', B1)
    print('数组C1：', C1)


# 第4题
def fun4(A, B, C):
    import numpy as np
    A2 = A.tolist()
    B2 = B.tolist()
    C2 = C.tolist()
    print('数组A2：', A2)
    print('数组B2：', B2)
    print('数组C2：', C2)

# 第5题
# hxy 是奇数 A1 B1
# 杨奥 是偶数 A B
def fun5(A,B):
    result=A+B
    print("A+B为:",result)

# 第六题
# 这个地方A是矩阵
def fun6(A):
    import numpy as np
    # 如果是A1则注释掉下面这一行,其他的不变
    # A=np.matix(A)
    import numpy as np
    A_max=A.max()
    A_min=A.min()
    # 按照最后一列降序排列
    A_up=A[np.lexsort(A.T)]
    A_down=A[np.lexsort(-A.T)]
    print('A_max为',A_max)
    print('A_min为',A_min)
    print('按照最后一列升序的',A_up)
    print('按照最后一列降序的',A_down)

# 第七题
def fun7(B):
    # 如果是B1则注释掉下面这一行,其他的不变
    # B=mat(B)
    B_3c_3r=B[3,3]
    B_2r=B[2,:]
    print('B的3行3列：',B_3c_3r)
    print('B的第二行：',B_2r)

#7请使用Python生成一个y+1行x+1列元素为1的矩阵、生成一个y+1行x+1列元素为0的数组、
#随机生成一个y+1行x+1列的数组、自动生成一个y+1行x+1列的单位矩阵
def fun7_2(x,y):
    from numpy import mat
    import numpy as np
    mat_1=mat(np.ones((x+1,y+1))) #元素为1矩阵
    array_0=np.zeros((x+1,y+1))   #元素为0数组
    rand_=np.random.rand(x+1,y+1) #随机矩阵，范围(0,1)数组
    mat_identity=np.identity(y+x) #单位矩阵
    print('mat_1为',mat_1)
    print('array_0为',array_0)
    print('rand_为',rand_)
    print('mat_identity为',mat_identity)

#8请使用Python查找(A+B)*C中大于a+b+c的索引
def fun8(A,B,C,a,b,c):
    import numpy as np
    mat_search=(A+B)*C
    index_=np.argwhere(mat_search > a+b+c)
    print('索引为',index_)

#9使用if语局计算分段函数在x=-2：0.1：5上的函数值
def fun9(a,b,c):
    import math
    import numpy as np
    e=math.exp(1)
    dic = {}
    dic['X'] = []
    dic['F(x)'] = []
    for ii in range (-20,50):
        if ii>10:
            ii=ii/10
            fx=np.sin(a*ii)
            dic['X'] .append(ii)
            dic['F(x)'] .append(fx)
        elif 5<ii<=10:
            ii=ii/10
            fx=1-b*np.power(ii,2)
            dic['X'] .append(ii)
            dic['F(x)'] .append(fx)
        else:
            ii=ii/10
            fx=np.power((1+c*ii),e)
            dic['X'] .append(ii)
            dic['F(x)'] .append(fx)
# 第10题
def fun10(a,b):
    import numpy as np
    W1 = np.random.randint(0,10,size=(a*a,b*b))
    W2 = np.random.randint(0,10,size=(a*a,b*b))
    # 先转成列表，然后在遍历
    W1=W1.tolist()
    W2=W2.tolist()
    for i in range(len(W1)):
        for j in range(len(W1[i])):
            if( W1[i][j] >0.3):
                # 取反
                W1[i][j]=-(W1[i][j])
    W=np.mat(W1)
    print('for循环转换W的结果如下：',W)
    i=0
    while(i<len(W2)):
        j=0
        while(j<len(W2[i])):
            if( W2[i][j] >0.3):
                # 取反
                W2[i][j]=-(W2[i][j])
            j+=1
        i+=1
    W=np.mat(W2)
    print('while循环转换W的结果如下：',W)

if __name__=='__main__':
    # 在这里可以输出所有题目的结果 根据题意依次调用
    fun1(x=9,y=4,z=8)
    a=27
    b=14
    c=25
    fun2(27,14,25 ,5)
    A=fun2(27,14,25 ,5)[0]
    B=fun2(27,14,25 ,5)[1]
    C=fun2(27,14,25 ,5)[2]
    fun4(A,B,C)
    fun5(A,B)
    fun6(A)
    fun7(B)
    # 自己输入自己的 x,y
    fun7_2(9,4)
    fun8(A,B,C,a,b,c)
    fun9(a,b,c)
    fun10(a,b)

