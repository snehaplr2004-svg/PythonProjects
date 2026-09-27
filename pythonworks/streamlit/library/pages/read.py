import streamlit as st

st.title("Read all book record")

from library_db import BookListCreateRetrieveUpdateDelete

b=BookListCreateRetrieveUpdateDelete()
records=b.list()
    # print("HELLO")
    # print(records)
st.table(records)