# 导入相关包
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state

# 数据载入模块
t0 = time.time()
X,y = fetch_openml("mnist_784",version=1,return_X_y=True)  # Load data from https://www.openml.org/d/554 
print(X.shape,y.shape) # (70000, 784) (70000,)

"""
在matplotlib中，整个图像为一个Figure对象。在Figure对象中可以包含一个或者多个Axes对象。
每个Axes(ax)对象都是一个拥有自己坐标系统的绘图区域。
"""
# fig, ax = plt.subplots(nrows=2,ncols=5) 
# ax = ax.flatten()  # flatten()将ax由2*5的Axes组展平成1*10的Axes组
# for i in range(10):
#     img = X[y == str(i)][0].reshape(28, 28) # 将img从1*784重构成28*28的数组
#     ax[i].imshow(img, cmap='Greys', interpolation='nearest')
#     ax[i].set_xticks([])
#     ax[i].set_yticks([])
#     ax[i].set_xlabel("Class %i" % i)
# plt.tight_layout() # 作用是自动调整子图参数,使之填充整个图像区域
# plt.show()


# random_state = check_random_state(0)  # 随机数种子
# permutation = random_state.permutation(X.shape[0]) # 随机排列数组，打乱样本
# X = X[permutation]
# y = y[permutation]
# print(X.shape) # (70000, 784)
#X = X.reshape((X.shape[0],-1))






train_samples = 5000 # 自定义训练样本的个数
x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=train_samples,test_size=10000) # 拆分验证集
print(x_train.shape) # (5000, 784)




scaler = StandardScaler() # 数据归一化
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)



"""
LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, 
class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)
正则化参数penalty: 可选择的值为"l1"和"l2"，分别对应L1的正则化和L2的正则化，默认是L2的正则化。
优化算法参数solver: 决定了对逻辑回归损失函数的优化方法，有5种算法可以选择，分别是：　“liblinear”, “newton-cg”, “lbfgs”, “sag” and “saga”。
分类方式参数multi_class: 有ovr和multinomial两个值可以选择，默认是ovr。ovr即one-vs-rest(OvR)，multinomial即many-vs-many(MvM)。
类型权重参数class_weight: 用于标示分类模型中各种类型的权重，不输入表示所有类型的权重一样。
如果class_weight选择balanced，那么类库会根据训练样本量来计算权重。某种类型样本量越多，则权重越低，样本量越少，则权重越高。
"""
clf = LogisticRegression(C=50./train_samples,multi_class="ovr", 
                         penalty="l1 ",solver="saga",tol=0.01)  # 逻辑回归分类器
clf.fit(x_train,y_train)
sparsity = np.mean(clf.coef_==0)*100  # clf.coef.shape (10, 784) 稀疏度，相关性为0的列统计
score = clf.score(x_test,y_test) # 返回测试数据和标签的平均精度
print("Best C %.4f" % clf.C) # 正则化系数
print("Sparsity with L1 penalty:%.2f%%"% sparsity)
print("Test score with L1 penalty:%.4f"% score)
# coef = clf.coef_.copy()
# plt.figure(figsize=(10,5))
# scale = np.abs(coef).max()
# for i in range(10):
#     l1_plot = plt.subplot(2,5,i+1)
#     l1_plot.imshow(coef[i].reshape(28,28),interpolation="nearest",
#                    cmap=plt.cm.RdBu,vmin=-scale,vmax=scale) # 相关性系数矩阵的可视化
#     l1_plot.set_xticks(())
#     l1_plot.set_yticks(())
#     l1_plot.set_xlabel("Class %i" % i)
# plt.suptitle("Classification vector for ...")
run_time = time.time()-t0
print("Example run in %.3f s" % run_time)
plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_digits
# from sklearn import metrics
# # 划分训练与测试数据集
# from sklearn.model_selection import train_test_split

# # Logistic Regression Classified
# def logistic_regression_classifier(x_train, y_train):
#     from sklearn.linear_model import LogisticRegression
#     model = LogisticRegression()
#     model.fit(x_train, y_train)
#     return model

# # Showing the image and the Labels(Digits Dataset)
# def plot_figure():

#     plt.figure()
#     # zip 数据打包为元组形式
#     for index, (image, label) in enumerate(zip(digits.data[0:5],digits.target[0:5])):
#         plt.subplot(1, 5, index + 1)
#         plt.imshow(np.reshape(image, (8, 8)))
#         plt.title("Training:%i\n" % label)
#     plt.show()

# if __name__ == "__main__":
#     digits = load_digits()

#     # Print to show there are 1797 images(8*8)
#     print("Image Data Shape = ", digits.data.shape)
#     # Print to show There are 1797 labels (intergers form 0-9)
#     print("Label Data Shape = ", digits.target.shape)

#     #绘制部分图片
#     plot_figure()

#     # 划分训练与测试数据集
#     x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

#     # 搭建模型
#     model = logistic_regression_classifier(x_train, y_train)

#     # 预测数据
#     predictions = model.predict(x_test)

#     # Measuring Model Performance
#     # 测试正确率，方案 ①
#     accuracy = metrics.accuracy_score(y_test, predictions)
#     print('accuracy: %.2f%%' % (100 * accuracy))

#     # 测试正确率，方案 ②，同方案1 一致
#     score = model.score(x_test, y_test)
#     print("score：%.2f%%" % (100 * score))