import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#load dataset
X,y = fetch_openml("mnist_784",version=1,return_X_y=True)  # Load data from https://www.openml.org/d/554 
print(X.shape,y.shape) # (70000, 784) (70000,)


train_samples = 5000 # the number of data for training
x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=train_samples,test_size=1000)
print(x_train.shape) # (5000, 784)


scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


clf = LogisticRegression(C=50./train_samples,multi_class="ovr",penalty="l1",solver="saga",tol=0.01)
clf.fit(x_train,y_train)
sparsity = np.mean(clf.coef_==0)*100
score = clf.score(x_test,y_test)


print("Best C %.4f" % clf.C) 
print("Sparsity with L1 penalty:%.2f%%"% sparsity)
print("Test score with L1 penalty:%.4f"% score)