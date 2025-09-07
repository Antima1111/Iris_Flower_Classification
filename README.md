# Iris Flower Classification

**Project Overview:**  
This is a simple machine learning project to classify Iris flowers using the **Random Forest** algorithm. The project predicts the species of Iris flowers based on their measurements: **sepal length, sepal width, petal length, and petal width**.  

**Algorithm Used:**  
- **Random Forest Classifier** – an ensemble of decision trees that votes for the final prediction.  
- Advantages: High accuracy, handles overfitting better than a single decision tree.

---

## **Dataset**
- The dataset used is `iris.csv`.  
- Columns:
  - `SepalLengthCm`
  - `SepalWidthCm`
  - `PetalLengthCm`
  - `PetalWidthCm`
  - `Species`
- The dataset contains 150 rows of Iris flowers across three species:
  - Iris-setosa
  - Iris-versicolor
  - Iris-virginica

---

## **How the Project Works**
1. **Load the CSV file** using `pandas`.  
2. **Select features** (`SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, `PetalWidthCm`) and **target** (`Species`).  
3. **Convert target labels** to numerical values using `LabelEncoder`.  
4. **Split dataset** into training and testing sets (80% train, 20% test).  
5. **Train Random Forest Classifier** on training data.  
6. **Evaluate model accuracy** on test data.  
7. **Save trained model** using `joblib` for future predictions.  
8. **Demo prediction**: Test the model with a sample flower measurement.  

---

## **How to Run**
1. Install required libraries:  
pip install pandas scikit-learn joblib

2. Make sure iris.csv and iris_classification.py are in the same folder.

3. Run the script:

python iris_classification.py

---

## **Sample Output**

First 5 rows of the dataset:

| Id | SepalLengthCm | SepalWidthCm | PetalLengthCm | PetalWidthCm | Species      |
|----|---------------|--------------|---------------|--------------|--------------|
| 1  | 5.1           | 3.5          | 1.4           | 0.2          | Iris-setosa  |
| 2  | 4.9           | 3.0          | 1.4           | 0.2          | Iris-setosa  |
| 3  | 4.7           | 3.2          | 1.3           | 0.2          | Iris-setosa  |
| 4  | 4.6           | 3.1          | 1.5           | 0.2          | Iris-setosa  |
| 5  | 5.0           | 3.6          | 1.4           | 0.2          | Iris-setosa  |


**Label mapping:** {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

**Model Accuracy:** 100.00%

**Demo prediction for [5.1, 3.5, 1.4, 0.2] is 'Iris-setosa'**

---

## **Files in the Repository**

iris_classification.py → Python script for training and prediction

iris.csv → Dataset

iris_model.pkl → Saved trained model (generated after running the script)

README.md → Project documentation

---

## **Submitted by :** 

**NAME : Antima Samokhu Prajapati**

**OASIS INFOBYTES INTERNSHIP**

**TASK 1 - IRIS FLOWER CLASSIFICATION**


