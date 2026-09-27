import streamlit as st
st.title(" Read a Book Record")

id=st.number_input("Book ID",min_value=0)
btn=st.button("Retrieve")
from library_db import BookListCreateRetrieveUpdateDelete

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(id)
    # st.table(record)
    st.title("Book Details")
    if record:
        st.write("Book ID:",record[0])
        st.write(f"Title:{record[1]}")
        st.write("Author:",record[2])
        st.write("Pages:",record[3])
        st.write("Price:",record[4])
        st.write("Language:",record[5])
    else:
        st.error("No record found")
