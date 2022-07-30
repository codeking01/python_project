# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from numpy import mat
import copy
import math
import warnings
import multiprocessing as mp
import joblib
import scipy.io
#
def r_2(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    r2=np.sum(np.multiply(x-x_mean,y-y_mean))**2/np.sum(np.power(x - x_mean,2))/np.sum(np.power(y - y_mean,2))
    return r2

warnings.filterwarnings("ignore")
cd_o=os.getcwd()
cd_p=os.path.dirname(cd_o)
cd_p1=os.path.dirname(cd_p)
cd_e=cd_p+'/data_excel/'
cd_n=cd_p+'/data_npy/'

data_a= pd.read_excel(cd_e+r"density.xlsx",sheet_name='data')
L=np.shape(data_a)[0]
Y=mat(data_a['Property']).T
T = mat(data_a['Temperature, K']).T
P = mat(data_a['Pressure, kPa']).T
T_SS = mat(data_a['select']).T
name_Cation = data_a['Cation']
N_Cation = mat(data_a['N_Cation']).T
N_Anion = mat(data_a['N_Anion']).T
XL_cation= mat(data_a['XL_cation']).T###
XL_anion= mat(data_a['XL_anion']).T###
XL_IL= mat(data_a['XL_IL']).T###
X_S=np.load(cd_n+'NI.npz',allow_pickle=True)
X_cation_S=mat(X_S['NI_S_Cation'])
X_anion_S=mat(X_S['NI_S_Anion'])
X_IL_S=mat(X_S['NI_S_ILs'])
X_IL_M_S=mat(X_S['NI_M_S'])
name_NI_S=mat(X_S['name_NI_S'])

ii_left_s=np.load(cd_n+'ii_left_s.npy')
name_NI_M_S= ['n_atom','n_atom-nnH','mw','st_m','st_s'] 

name_NI_S_s=name_NI_S.tolist()[0]
name_NI_S_s_0=copy.deepcopy(name_NI_S_s)
name_NI_S_s_1=copy.deepcopy(name_NI_S_s)
name_NI_S_s_2=copy.deepcopy(name_NI_S_s)
for i in range(0,len(name_NI_S_s)) :
    name_NI_S_s_0[i]=name_NI_S_s_0[i]+'_C'
    name_NI_S_s_1[i]=name_NI_S_s_1[i]+'_A'
    name_NI_S_s_2[i]=name_NI_S_s_2[i]+'_ILs'
name_NI_S_s_all=np.mat(name_NI_S_s_0+name_NI_S_s_1+name_NI_S_s_2+name_NI_M_S)
name_NI_S_s=name_NI_S_s_all[:,ii_left_s].tolist()[0]
name_NI_S_s_T=copy.deepcopy(name_NI_S_s)
name_NI_S_s_T_=copy.deepcopy(name_NI_S_s)
name_NI_S_s_P=copy.deepcopy(name_NI_S_s)

for i in range(0,len(ii_left_s)) :
    name_NI_S_s_T[i]=name_NI_S_s_T[i]+'*T'
    name_NI_S_s_T_[i]=name_NI_S_s_T_[i]+'/T'
    name_NI_S_s_P[i]=name_NI_S_s_P[i]+'*P'
  
name_NI_S_s=np.mat(name_NI_S_s+name_NI_S_s_T+name_NI_S_s_T_+name_NI_S_s_P)
XT_S=copy.deepcopy(np.c_[X_IL_S, np.multiply(X_cation_S,N_Cation),np.multiply(X_anion_S,N_Anion),np.sqrt(X_IL_M_S)])
 
XT_S_d=XT_S[:,ii_left_s]

XT_S_d_T = np.multiply(copy.deepcopy(XT_S_d),T)
XT_S_d_T_ = copy.deepcopy(XT_S_d)/T
XT_S_d_P = np.multiply(copy.deepcopy(XT_S_d),P)
XT_SDM_d=np.c_[XT_S_d, XT_S_d_T, XT_S_d_T_,XT_S_d_P,T,1/T,P]

x_0=np.sum(XT_SDM_d,1)
SS_w=np.where((T_SS==1)&(x_0!=0)&(~np.isnan(Y)))[0]

#SS_w=np.where((T_SS==1)&(x_0!=0)&(~np.isnan(Y)))[0]
name_Cation=name_Cation.iloc[SS_w]

tt = np.ones((len(name_Cation),1))

Y=Y[SS_w,:]
XT_SDM_d=XT_SDM_d[SS_w,:]
XLA=XL_cation[SS_w,:]  ###引入XLA
XLB=XL_anion[SS_w,:]  ###引入XLB
XLC=XL_IL[SS_w,:]  ###引入XLC

#P_Cation = name_Cation.value_counts(normalize=True)
P_Cation = name_Cation.unique()
p_ILs = []
for i in P_Cation:
    n_w = np.where(name_Cation==i)[0]
    n_w_l = len(n_w)
    p_ILs.append([n_w_l,i])
p_ILs.sort(reverse = True) 
p_ILs=pd.DataFrame(p_ILs)
P_ara = np.arange(1,np.shape(p_ILs)[0],5)
P_Cation_i = p_ILs.iloc[P_ara,1]
n_Cation_i = p_ILs.iloc[P_ara,0]
su=sum(n_Cation_i)/len(name_Cation)
print(su)
for i in P_Cation_i:
    nw = np.where(name_Cation==i)
    tt[nw,:]=-1

tt_1 = np.where(tt==-1)[0]
tt1 = np.where(tt==1)[0]

Y_test = Y[tt_1,:]
XT_SDM_d_test=XT_SDM_d[tt_1,:]
XLA_test=XL_cation[tt_1,:]  ###引入XLA
XLB_test=XL_anion[tt_1,:]  ###引入XLB
XLC_test=XL_IL[tt_1,:]

Y_train = Y[tt1,:]
XT_SDM_d_train=XT_SDM_d[tt1,:]
XLA_train=XL_cation[tt1,:]  ###引入XLA
XLB_train=XL_anion[tt1,:]  ###引入XLB
XLC_train=XL_IL[tt1,:]

x_0_=np.sum(XT_SDM_d_train,0)
w_x_0_=np.where(x_0_==0)[1]

print([su,min(Y_train)[0,0],max(Y_train)[0,0],min(Y_test)[0,0],max(Y_test)[0,0]])

if len(w_x_0_)>0:
    print('请调整训练集与测试集',w_x_0_)
    

