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
>#### Output of the Code: [21,2]
Here there shown shape of the Dataset. It shows 2D/3D/4D information as follows (x,y)/(x,y,z)/(p,q,r,s) etc  
- If the Dataset contain 2D Data, means Tabular/ Matrix Data then it will shows 2 information as Row and Column  
- If the Dataset contain 3D Data as RGB Image then it will shows 3 infoormation as Height, Width, Channel  


**What is the meaning of of the Output: [21,2]**  
- 15 means there are  15 sample or row
- 2 means there are 2 features or column

### **Features & Sample Number**
From the previous code we can find the features and sample by using .shape. So here an Array indicates the total Sample and total Features. This Array is Zero indexed Array. So 
```
print("Number of Sample/ Row: ",dataset.shape[0])

print("Number of Features/ Column: ",dataset.shape[1])
```
>#### Output of the Code:
>Number of Sample/ Row: 21  
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
>Shape of the Dataset:  (21, 2)  
>Total number of Sample/ Row: 21  
>Total number of Features/ Column: 2  
>Comumns Name:  Index(['area', 'price'], dtype='object')  
>Features:  area  
>True Target:  price  

<h2 align="center">Pre Processing Steps</h2>

## Step 1) Check & Handeling the Duplicate Vale:  
Now we  should check is there any duplicate vales are available or not. 
### Checking Duplicate value: 
```
dataset.duplicated()
```
>#### Output of the Code:
>True/ False  
> Here Ture means that particular sample is duplicated means same samples is available in the upper ption

### Checking total Number of duplicate value
```
print("Total Number of duplicate: ",dataset.duplicated().sum())
```
>#### Output of the Code:
>Total Number of duplicate:  11  
This means that there are 11 duplicate values. 

### Checking percentages of duplicate value: 
now we need to check what is the percentages of duplicate value out of teh entire dataset. So the formula will be 
$$
\frac{total Duplicate}{total sample}*100%
$$
```
totalDuplicate=dataset.duplicated().sum()
print("Percentages of Duplicate values: ", (totalDuplicate/dataset.shape[0] * 100))
```
>#### Output of the Code:
> Percentages of Duplicate values:  52.38095238095239

### Handeling duplicate value: 
Although duplicate values are unnecessary samples which are not /extra effective in your model.So we need to drop the entire cell or sample which are duplicated. 
```
dataset=dataset.drop_duplicates()
```
Here I drop the duplicate cell and after deplicate i replace the dataset variable. 

Now again check the duplicated are removed or not. 
### Checking total Number of duplicate value
```
print("Total Number of duplicate: ",dataset.duplicated().sum())
```
>#### Output of the Code:
>Total Number of duplicate:  0  