### 11_machine_learning.py ###
# all the code in here is executed in Anaconda Jupyter notebook
#
# scikit-learn - machine learning in Python
#
#
#
import matplotlib.pyplot as plt
from sklearn import tree
import joblib  # import directly
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
df = pd.read_csv('vgsales.csv')     # return data frame
# nubmers of rows and columns
print(df.shape)  # (16598, 11) Jupyter doesn't need print()
# basic statistic info of each columns (ie. count, mean, std, min, max)
# if the count value is different, some rows may not have the values for that column
# mean - average, std - standard deviation
df.describe()
#
# return 2-D array
df.values
#
#

music_data = pd.read_csv('music.csv')     # return data frame
music_data

# seperate the data into input and output dataset
# input: age and gender
# output: genre
#

### using Jupyter ###
#import pandas as pd
df = pd.read_csv('http://bit.ly/autompg-csv')
df.head()

%matplotlib inline
df.plot.scatter(x='hp', y='mpg')


### build a model ###

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)
# prediction what genre for age 21 male and age 22 female
predictions = model.predict([[21, 1], [22, 0]])
predictions         # output:array(['HipHop', 'Dance'], dtype=object)


### split the input data and target result ###
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
# split training data and testing data (ie. 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# select the model
model = DecisionTreeClassifier()
# train the model - use 80% of dataset
model.fit(X_train, y_train)
# prediction what genre for age 21 male and age 22 female
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)
score
# Ctrl+Enter to run multiple times
# as the train_test_split is randomly pick the data
# sometimes the output is not 100% correct (ie. 1.0)
# it may down to 25% (ie. 0.25) is very small


### presisting the model ###
### use entire dataset to train ###
# from sklearn.externals import joblib #deprecated on scikit-learn 0.21

music_data = pd.read_csv('music.csv')

# separate data and result columns
X = music_data.drop(columns=['genre'])
y = music_data['genre']

# build the model
model = DecisionTreeClassifier()

# training it (use entire dataset)
model.fit(X, y)

# presisting model #
joblib.dump(model, 'music-recommender.joblib')


# prediction what genre for age 21 male and age 22 female
#predictions = model.predict([[21, 1], [22, 0]])
# predictions         # output:array(['HipHop', 'Dance'], dtype=object)


### Visualizing a Decision Tree ###

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
model = DecisionTreeClassifier()
model.fit(X, y)

# DOT - graph descriptions language of the Graphviz graph
# feature_names - the columns of dataset
# class_names - unique set of the name of result
# label='all' - show all label in each rectangle
# rounded - rounded corner of the rectangle
# filled - filled with color

tree.export_graphviz(model, out_file='music-recommender.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)
#
# drap and drop the .dot file to Visual Studio Code
# install VS Code extension
# Graphviz (dot) language support for Visual Studio Code by Joao Pinto
#
#
#
