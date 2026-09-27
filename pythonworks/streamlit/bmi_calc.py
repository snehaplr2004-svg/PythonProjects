# import streamlit as st
#
# st.title("Bmi Calculator")
#
# weight=st.number_input("enter weight in kg")
# height=st.number_input("enter height in cm")
# btn=st.button("Calculate")
#
# if btn:
#     b=weight/((height/100)**2)
#
#     st.write("BMI is",b)
#     if b<18.5:
#         st.info("underweight")          #st.write("Underweight")..... special thing are
#                                         # given to display with special colour for each case
#     elif 18.5<=b<25:
#         st.success("normal")
#     elif 25<=b<30:
#         st.warning("overweight")
#     else :
#         st.error("obesity")
#
import email

import streamlit as st

from datetime import date
name=st.text_input("enter your name")
age=st.number_input("enter your age")
DOB=st.date_input("enter your date of birth",min_value=date(1990,1,1),
                  max_value=date.today(),
                  value=date(2000,1,1))
email=st.text_input("Enter email")
gender=st.radio("Gender",["Male","Female"])
course=st.selectbox("Course",["python","java","dotnet","testing"])

btn=st.button("Register")
if btn:
    st.title("STUDENT REGISTRATION FORM")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",DOB)
    st.write("Email:",email)
    st.write("Gender:",gender)
    st.write("Course:",course)