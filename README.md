<h1 align="center">Home Price Prediction</h1>

## Step 1) Load The Dataset: 
Let say We have the dataset called "dhaka_homeprices.csv". Now we need to load the dataset. For load the Dataset we need a library as named **Pandas**. So firstly install the dataset using the command in terminal.  
NB: You need to install only for the first time
```
pip install pandas
```
* Now import the pandas library
* Load the dataset using the inner function called **.read_csv()**
```
import pandas as pd

dataset=pd.read_csv("dhaka_homeprices.csv")
```
NB: Replace the dataset name with yours. Make sure that your datasets are in same folder. 

## Step 2) Information of the Dataset: 
Check the Shape (Features, Sample, Features Name)  
### **Shape of the Dataset**
```
print("Shape of The Dataset",dataset.shape)
```
>#### Output of the Code: [15,2]
Here there shown shape of the Dataset. It shows 2D/3D/4D information as follows (x,y)/(x,y,z)/(p,q,r,s) etc  
- If the Dataset contain 2D Data, means Tabular/ Matrix Data then it will shows 2 information as Row and Column  
- If the Dataset contain 3D Data as RGB Image then it will shows 3 infoormation as Height, Width, Channel  


**What is the meaning of of the Output: [15,2]**  
- 15 means there are  15 sample or row
- 2 means there are 2 features or column

### **Features & Sample Number**
From the previous code we can find the features and sample by using .shape. So here an Array indicates the total Sample and total Features. This Array is Zero indexed Array. So 
```
print("Number of Sample/ Row: ",dataset.shape[0])

print("Number of Features/ Column: ",dataset.shape[1])
```
>#### Output of the Code:
>Number of Sample/ Row: 15  
>Number of Features/ Column: 2

### **All the Features Name**
Now we need fo find all the features name. We can manually check the features name but if the dataset have a lot of features, its useful to find the features name using code. 

```
print("Features Name: ",dataset.columns)
```
>#### Output of the Code:
>Features Name:  Index(['area', 'price'], dtype='object')  

So here there two features one is area and another is price. Now we can easily extract our Features and True Target

```
print("Features: ", dataset.columns[0])
print("True Target:", dataset.columns[1])
```
>#### Output of the Code:
>Features:  area  
>True Target: price

### **All a glance all the Informations are**
```
## All the information
print("Shape of the Dataset: ", dataset.shape)
print("Total number of Sample/ Row:",dataset.shape[0])
print("Total number of Features/ Column:",dataset.shape[1])
print("Comumns Name: ", dataset.columns)
print("Features: ",dataset.columns[0])
print("True Target: ", dataset.columns[1])
```
>#### Output of the Code:
>Shape of the Dataset:  (9, 2)  
>Total number of Sample/ Row: 9  
>Total number of Features/ Column: 2  
>Comumns Name:  Index(['area', 'price'], dtype='object')  
>Features:  area  
>True Target:  price  
