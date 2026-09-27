import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

tab1,tab2,tab3,tab4,tab5=st.tabs(["ADD","READ","RETRIEVE","DELETE","UPDATE"])
b=BookListCreateRetrieveUpdateDelete

with tab1:
    st.title("Add")
with tab2:
    st.title("Read")
with tab3:
    st.title("Retrieve")
with tab4:
    st.title("Delete")
with tab5:
    st.title("Update")