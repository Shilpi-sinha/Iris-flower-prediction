from django.shortcuts import render
from emp.forms import *
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
# Create your views here.
def show(request):
	if request.method=='POST':
		frm=EmployeeForm(request.POST)
		s1=request.POST['s1']
		sw=request.POST['sw']
		p1=request.POST['p1']
		pw=request.POST['pw']	
		data=pd.read_csv('iris.csv',names=['s1','sw','p1','pw','type'])
		x=data.iloc[:,0:4]
		y=data['type']
		x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=12)
		knn=KNeighborsClassifier(n_neighbors=5)
		knn.fit(x_train,y_train)
		test=[[s1,sw,p1,pw]]
		testdata=pd.DataFrame(test)
		prediction=knn.predict(testdata)
		return render(request,'predict.html',{'p':prediction})
	else:
		frm=EmployeeForm()
	return render(request,'index.html',{'e':frm})
