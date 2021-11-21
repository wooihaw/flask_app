from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv
from joblib import dump


df = read_csv(
    "https://raw.githubusercontent.com/wooihaw/datasets/main/heights_weights_genders.csv"
)
X = df.values[:, :-1]
y = df.values[:, -1]
knn = KNeighborsClassifier().fit(X, y)
print(knn.predict([[175, 80]]))

# Serialize model to file
dump(knn, "model.joblib")
