from sklearn.datasets import load_digits
digits = load_digits()
digits.images.shape

X = digits.data
y = digits.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)

from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)


from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred,y_test))










import matplotlib.pyplot as plt
fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                                 subplot_kw={'xticks':[], 'yticks':[]},
                                 gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i, ax in enumerate(axes.flat):
            ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
            ax.text(0.05, 0.05, str(digits.target[i]),
            transform=ax.transAxes, color='green')
