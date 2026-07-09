import streamlit as st
import requests

st.set_page_config(
    page_title="BLOOD TEST REPORT ANALYSIS",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 BLOOD TEST REPORT ANALYSIS")

menu = st.sidebar.selectbox("Menu",["New Patient","Get Patient Details","Update Patient Details","Remove Patient"])

if menu == "New Patient":
    st.subheader("Patient Details")
    full_name = st.text_input("Full Name")
    date_of_birth = st.date_input("Date of Birth")
    email_address = st.text_input("Email Address")
    st.subheader("Blood Test Values")
    glucose = st.number_input("Glucose (mg/dL)", min_value=0.0)
    haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0)
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0)

    if st.button("Generate Health Report"):
        payload = {
        "full_name": full_name,
        "date_of_birth": str(date_of_birth),
        "email_address": email_address,
        "glucose": glucose,
        "haemoglobin": haemoglobin,
        "cholesterol": cholesterol  }
         
        response = requests.post(
         "http://127.0.0.1:8000/add_patient",
          json=payload)
        
        if response.status_code == 200:
            
            st.success("Report Generated Successfully")
            st.subheader("AI Health Remarks")
            st.write(response.json())
        else:
            st.text(response.text)


elif menu == "Get Patient Details":
    st.header("Search Patient")
    full_name =st.text_input("Enter Patient Name")
    email_address = st.text_input("Enter Email Address")
    if st.button("Search"):
        response = requests.get("http://127.0.0.1:8000/get_patient",
                               params={
                                   "patient_name": full_name,
                                   "email_address": email_address
                               })

        if response.status_code == 200:
            data = response.json()
            st.subheader("Patient Details")
            st.text(f"Full Name: {data['full_name']}")
            st.text(f"Date of Birth: {data['date_of_birth']}")
            st.text(f"Email Address: {data['email_address']}")
            st.text(f"Glucose: {data['glucose']} mg/dL")
            st.text(f"Haemoglobin: {data['haemoglobin']} g/dL")
            st.text(f"Cholesterol: {data['cholesterol']} mg/dL")
            st.subheader("AI Health Remarks")
            st.text(data["remarks"])
        else:
            st.text(response.text)

elif menu == "Update Patient Details":
    full_name = st.text_input("Enter Patient Name to Update")
    email_address = st.text_input("Enter Email Address to Update")
    if st.button("Search"):
        response = requests.get(
        "http://127.0.0.1:8000/get_patient",
        params={
            "patient_name": full_name,
            "email_address": email_address
               }
          )
        if response.status_code == 200:
            st.session_state["patient"] = response.json()
        else:
            st.error("Patient not found.")

    if "patient" in st.session_state:
        data = st.session_state["patient"]

        full_name = st.text_input("Full Name", value=data["full_name"])
        date_of_birth = st.text_input("Date of Birth", value=data["date_of_birth"])
        email_address = st.text_input("Email", value=data["email_address"])

        glucose = st.number_input(
        "Glucose",
        value=float(data["glucose"])
        )

        haemoglobin = st.number_input(
        "Haemoglobin",
        value=float(data["haemoglobin"])
       )

        cholesterol = st.number_input(
        "Cholesterol",
        value=float(data["cholesterol"])
        )

        if st.button("Update Patient"):
            payload = {
           
            "full_name": full_name,
            "date_of_birth": date_of_birth,
            "email_address": email_address,
            "glucose": glucose,
            "haemoglobin": haemoglobin,
            "cholesterol": cholesterol
           }

            update_response = requests.put(
            "http://127.0.0.1:8000/update_patient",
            params={
                "patient_name": data["full_name"],
                "email_address": data["email_address"]
            }
            , json = payload
             )

            if update_response.status_code == 200:
                st.success("Patient updated successfully!")
                st.session_state["patient"] = update_response.json() 
            else:
                st.error(update_response.text) 

elif menu == "Remove Patient":
    full_name = st.text_input("Enter Patient Name to Delete")
    email_address = st.text_input("Enter Email Address to Delete")
    if st.button("Delete"):
        response = requests.delete(
        "http://127.0.0.1:8000/delete_patient",
        params={
            "patient_name": full_name,
            "email_address": email_address
        }
        )
        if response.status_code == 200:
            st.success("Patient deleted successfully!")
        else:
            st.error(response.text)
    
    
