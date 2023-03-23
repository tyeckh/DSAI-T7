import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt # we only need pyplot
from matplotlib.cbook import boxplot_stats
sb.set() # set the default Seaborn style for graphics

#sklearn libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

DrugData = pd.read_csv("Dataset/Drug.csv")
DrugData.head
