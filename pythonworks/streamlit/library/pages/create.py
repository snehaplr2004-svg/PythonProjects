import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title("Add new book record")

title=st.text_input("Title")
author=st.text_input("Author")
pag=st.number_input("Pages",min_value=0)
price=st.number_input("Price",min_value=0)
lang=st.text_input("Language")
btn=st.button("Add Book")

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,pag,price,lang)
    st.success("Record Created Successfully")