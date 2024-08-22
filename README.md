<h1 align="center">Home Price Prediction</h1>

#### Step 1) Load The Dataset: 
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