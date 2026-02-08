from Models.regression import LinearRegressionModel
from Models.classification import KNNModel
from Utils.metrics import accuracy_score

reg = LinearRegressionModel()
reg.fit([1,2,3],[10,20,30])
print(reg.predict([5,6]))

Knn=KNNModel()
Knn.train([1,2,3],["A","A","B"])
pred=Knn.predict([10,11])
print(pred)

score=accuracy_score(["A","A"], pred)
print("Accuracy:",score)