import streamlit as st

from Blood_Donor import BloodDonor

tab1,tab2,tab3,tab4,tab5=st.tabs(["ADD","READ","RETRIEVE","DELETE","UPDATE"])
b=BloodDonor()

with tab1:
    st.title("Add")
    name= st.text_input("Name")
    blood_group= st.selectbox("Blood Group",["A+","A-","B+","B-","O+","O-","AB+","AB-"])
    phone = st.text_input("Phone")
    city = st.text_input("City")
    last_donation = st.date_input("Last Donation")
    btn = st.button("Add Donor")

    if btn:
        b.post(name,blood_group,phone,city,last_donation)
        st.success("Record Created Successfully")
with tab2:
    st.title("Read")
    records = b.get()
    st.table(records)
with tab3:
    st.title("Retrieve")
    id = st.number_input("Donor ID", min_value=0)
    btn = st.button("Retrieve")
    if btn:
        record = b.retrieve(id)
        st.title("Donor Details")
        if record:
            st.write("Donor ID:", record[0])
            st.write(f"Name:{record[1]}")
            st.write("Blood Group:", record[2])
            st.write("Phone NUmber:", record[3])
            st.write("City", record[4])
            st.write("Last Donated:", record[5])
        else:
            st.error("No record found")

with tab4:
    st.title("Delete")
    id = st.number_input("Enter Donor ID", min_value=0)
    btn = st.button("Delete")

    if btn:
        rec = b.delete(id)
        if rec:
            st.success("Donor Deleted Successfully")
        else:
            st.error("Donor Not Found")
with tab5:
    st.title("Update")

    id = st.number_input("Enter donor id", min_value=0)
    na = st.text_input("Enter new donor name")
    bg = st.text_input("Enter new donor blood group")
    ph = st.text_input("Enter new donor phn no")
    cty = st.text_input("Enter new donor city")
    ld = st.date_input("Enter new donor last donated date")

    btn = st.button("Update")
    if btn:
        rec = b.put(id, na, bg,ph, cty, ld)
        if rec:
            st.success("Donor Updated Successfully")
        else:
            st.error("No record found")

