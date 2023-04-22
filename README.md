# A133 Team 7 Mini-Project | SC1015 AY22/23 Sem 2

## About
This is our Mini-Project for SC1015 which aims to analyze the dataset and identify significant factors that impact life expectancy, such as GDP, BMI, and HIV/AIDS prevalence. 


Do take a look at the powerpoint slides for a detailed walkthrough of our project!

## Contributors
 - Chan Kit Ho ([@tyeckh](https://github.com/tyeckh)): Data Preparation and Exploratory Data Analysis
 - Chiang Qin Zhi ([@chqizh](https://github.com/chqizh)): Exploratory Data Analysis and Machine Learning


## Motivation 
Our motivation for this project is to investigate the various demographic, health, and socio-economi factors that impact life expectancy and recommend improvements through predictive models.  
  
Through inital analysis of the data, we note that the average life expectancy have rise over the years, however there still exist a large disparity in life expectancy across different regions. Through our project, we hope to gain insights into the factors that have significant impacts on life expectancy, and identify areas that require further attention and intervention.  
  
Ultimately, with a better understanding of the factors and an effective machine learning prediction model, it would aid in the development of better public health policies and practices and promote a better quality of life for people across different regions and countries.

## Problem Definiton
 - What are main factors that affects life expectancy around the world
 - How can the disparity in life expectancy be addressed effectively and efficiently across different regions
 - Which of the ML Models that we employ is the most effective in predicting life expectancy

## Datasets
- [Life Expectancy (WHO) Fixed](https://www.kaggle.com/datasets/lashagoch/life-expectancy-who-updated)

## Machine Learning Algorithms used
- Multivariate Linear Regression (Regression)
- Decision Tree (Classification & Regression)
- Random Forest* (Regression)
- K-Neighbours** (Regression)
- Multi-Layer*** Perceptron ANN (Regression)

<i>&nbsp; &nbsp; We used the scikit-learn library for the models: </i>
<br> &nbsp; &nbsp; *[Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) </br>
&nbsp; &nbsp; **[Multi-Layer Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)
<br> &nbsp; &nbsp; ***[K-Nearest Neighbours](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) </br>

## Conclusion
- Population size has minimum correlation with life expectancy, this is justified as population size may vary widely between countries with similar levels of life expectancy.
- Mortality Rates, Economic Status and Schooling are important variables as they have high correlation and linearity with life expectancy. Higher mortality rates likely indicate poorer health conditions, while higher levels of schooling are associated with better health awareness and access to healthcare. 
- Life expectancy can be a good classifying variable for Economic status of a country (Developing/Developed), signifying that economy status is a significant factor, which is backed up by the correlation and the rest of our models. This makes sense as the wealthier a country is, the better it's healthcare and working conditions for instance.
- Based on the models used, we derived that Random Forest returned the best model in predicting life expectancy.

## What did we learn from this project
- We made use of Random Forest Regressors, K-Neighbours Regressors and Multi-Layer Perceptron Neural Networks, which are new Machine Learning algorithms not taught in the course.
- We also learnt that technical complexity of a model does not equate to greater accuracy, in the case of the Multi-Layer Perceptron, with Linear Regression faring similarly well.
- We were able to apply Data science concepts taught in this course, like visualisation tools and tools to evaluate models.
- We also learnt about the usage of github and information about life expectancy.

## Special thanks
We would like to give appreciation to our Lab TA, Zou Yuxuan of NTU SCSE for being patient and responsive to our queries during our consultations in lab.

## References
https://www.kaggle.com/datasets/lashagoch/life-expectancy-who-updated
