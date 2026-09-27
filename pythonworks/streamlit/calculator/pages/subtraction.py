import streamlit as st
st.title("Subtraction")
num1=st.number_input("enter number1",min_value=0)
print(num1)             #print the data enterd in console
num2=st.number_input("enter number2",min_value=0)
print(num2)
btn=st.button("sub")        #create button
if btn:         #afr=ter clicking it work
    result=num1-num2
    print(result)       #got printed in console
    st.write("Difference is",result)    #got printed in interface
