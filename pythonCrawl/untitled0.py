#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:31:25 2018

@author: ikhwan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:50:10 2018

@author: EnSangJeon
"""
import pandas as pd
import numpy as np
import os

from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold

datapath = '/Users/ikhwan/downloads'
vote= pd.read_csv(os.path.join(datapath,'US_County_Level_Presidential_Results_12-16.csv'),index_col=0)
county=pd.read_csv(os.path.join(datapath,'county_facts.csv'))


merge=pd.merge(vote, county, left_on = 'FIPS', right_on = 'fips', how = 'left')

merge['target'] = (merge['votes_dem_2016']>merge['votes_gop_2016'])*1

merge['target'].value_counts()

merge.columns
ak = merge[merge['state_abbr']=='AK']

ak_mean=ak.mean().to_frame().T

data=pd.concat((merge[merge['state_abbr']!='AK'],ak_mean))


skfold = StratifiedKFold(shuffle = True, random_state = 10)
k=5

accs=[]
recall=[]
precision=[]
f1s=[]

accs2=[]
recall2=[]
precision2=[]
f1s2=[]

vars1=[x for x in data.columns if 'AGE' in x]
vars2 = [x for x in data.columns if 'INC' in x]
vars3 = [x for x in data.columns if 'RHI' in x]
vars = vars1+vars2+vars3
X=data[vars]
y=data['target']



from sklearn.svm import SVC
svc = SVC(kernel='linear')

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from imblearn.over_sampling import RandomOverSampler
ros= RandomOverSampler()
X_sampled1, y_sampled1 = ros.fit_sample(X, y)

for train_set, valid_set in skfold.split(X_sampled1,y_sampled1):
    svc = SVC(kernel='linear')
    svc.fit(X_sampled1[train_set],y_sampled1[train_set])
    y_pred1 = svc.predict(X_sampled1[valid_set])
    acc = accuracy_score(y_sampled1[valid_set], y_pred1)
    r= recall_score(y_sampled1[valid_set], y_pred1)
    p= precision_score(y_sampled1[valid_set], y_pred1)
    f1 = f1_score(y_sampled1[valid_set], y_pred1)
    accs.append(acc)
    recall.append(r)
    precision.append(p)
    f1s.append(f1)
    
    clf.fit(X_sampled1[train_set],y_sampled1[train_set])
    y_pred2 = clf.predict(X_sampled1[valid_set])
    acc2 = accuracy_score(y_sampled1[valid_set], y_pred2)
    r2 = recall_score(y_sampled1[valid_set], y_pred2)
    p2 = precision_score(y_sampled1[valid_set], y_pred2)
    f1_2 = f1_score(y_sampled1[valid_set], y_pred2)
    accs2.append(acc2)
    recall2.append(r2)
    precision2.append(p2)
    f1s2.append(f1_2)
    
