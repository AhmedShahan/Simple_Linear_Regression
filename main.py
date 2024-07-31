import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

def calculateRegression(dataset):
    x=dataset.iloc[:,:-1]
    y=dataset.iloc[:,-1:]
    model=LinearRegression()
    model.fit(x,y)
    b=model.coef_
    m=model.intercept_

    result=[m,b]
    return result

# Function to load the dataset
def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            return data
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return None
    return None

# Streamlit app
def main():
    st.title("Simple Linear Regression")

    st.write("Upload a CSV file to see the M & B")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        if data is not None:
            if st.button("SCalculate"):
                st.write("The Slope B : ")
                result=calculateRegression(data)
                print(type(result))
                st.write(result[0])
                print(type(result[0]))
                st.write("The Slope M : ")
                st.write(result[1])
                st.write("The Equation is: ")
                st.write(f"y = {round(result[1][0][0],2)} X + {round(result[0][0])}")
                # st.write(data.shape)
        else:
            st.write("Failed to load data.")

if __name__ == "__main__":
    main()
