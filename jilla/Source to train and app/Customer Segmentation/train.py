import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle



df= pd.read_csv('segmentation data.csv', index_col = 0)
scaler = StandardScaler()
df_std = scaler.fit_transform(df)

#𝐊-𝐦𝐞𝐚𝐧𝐬 𝐂𝐥𝐮𝐬𝐭𝐞𝐫𝐢𝐧𝐠 ----------------------------------------------------

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(df_std)
    wcss.append(kmeans.inertia_)

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
kmeans.fit(df_std)

#Result Of Our K-means DATA SET -----------------------------------------
final=df.reset_index(drop = True)
final['Segment K-means'] = kmeans.labels_

#Train Data---------------------------------------------------------------
x=final.iloc[:,[0,1,2,4,5,6]].values
y=final['Segment K-means'].values

train_x, test_x, train_y, test_y = train_test_split(x,y, test_size=0.2, random_state=0)
model = RandomForestClassifier(random_state=13)
model.fit(train_x, train_y)

predicted = model.predict(test_x)
model.score(test_x, test_y) #Our Score 0.9875

#Another Score algorithm for Our Machine algorithm-------------------------

# from sklearn.metrics import confusion_matrix

# probabilities = model.predict_proba(test_x)
# confusion_matrix(test_y, predicted)------------Our Score array([[ 36,   1,   2,   9],
                                                              #   [  2,  41,  34,  18],
                                                              #   [  3,  23, 108,   8],
                                                              #   [  3,   8,  11,  93]], dtype=int64)

# from sklearn.metrics import precision_score

# train_predictions = model.predict(train_x)
# precision_score(train_y, train_predictions, average='micro')------- #Our Score 1.0 ---------

pickle.dump(model, open('model.pkl', 'wb'))

pickled_model = pickle.load(open('model.pkl', 'rb'))
Sex=0
Marital_status=0
Age=45
# Education=1
Income=171565
Occupation=1
Settlement_size=1

predict=pickled_model.predict([[Sex,Marital_status,Age,Income,Occupation,Settlement_size]])
print(predict)