import streamlit as st

st.set_page_config(page_title="Encrypted Entry Code Page", page_icon =":material/drag_pan:")

#TitleDetails
st.title("Encrypted Entry Code Page")
st.write("Enter the correct safe word of the day in order to gain access to the dashboard credentials.")
st.write("**Please message the developer for the word assigned during the time of access.**")



#Sidebar Links
st.sidebar.image("MHLogo_White.png.png")
st.sidebar.title("Page Navigation")
st.sidebar.page_link("MasterDashboard.py",label="Master Dashboard")
st.sidebar.page_link("pages/EntryCodes.py",label="Encrypted Entry Code Page")

# A nice section for the protected download
st.markdown("---")
st.subheader("🗎 Encrypted Credential Access")
st.write("Document Code Hint: Alter ego Camera Model + BOLD + Birthdate!")

# Simple text input for family members
family_pass = st.text_input("Safe Word:", type="password")

# Your simple shared password
CORRECT_PASSWORD = st.secrets["correct_password"]

if family_pass == CORRECT_PASSWORD:
    st.success("Access Granted.")

    # Read the Word document into bytes safely
    try:
        with open("CredentialList.docx", "rb") as f:
            file_bytes = f.read()

        # Serve the file bytes via the download button
        st.download_button(
            label="Download Credential List",
            data=file_bytes,
            file_name="CredentialList.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except FileNotFoundError:
        st.error("Error: 'CredentialList.docx' could not be found in the project directory.")

elif family_pass:
    st.error("Wrong Password.")