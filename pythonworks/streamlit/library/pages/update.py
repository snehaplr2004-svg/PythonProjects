import streamlit as st
st.title(" Update book record")
from library_db import BookListCreateRetrieveUpdateDelete
id=st.number_input("Enter book id",min_value=0)
ti=st.text_input("Enter new book title")
au=st.text_input("Enter new book author")
pa=st.number_input("Enter new book pages")
pr=st.number_input("Enter new book price")
la=st.text_input("Enter new book language")

btn=st.button("Update")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    rec=b.update(id,ti,au,pa,pr,la)
    if rec:
        st.success("Book Updated Successfully")
    else:
        st.error("No record found")

