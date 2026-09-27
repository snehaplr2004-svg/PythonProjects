import streamlit as st
st.title("Delete Book Record")
id=st.number_input("Enter Book ID",min_value=0)
btn=st.button("Delete")
from library_db import BookListCreateRetrieveUpdateDelete
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    rec=b.delete(id)
    if rec:
         st.success("Book Deleted Successfully")
    else:
         st.error("Book Not Found")