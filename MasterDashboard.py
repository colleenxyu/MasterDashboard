import streamlit as st

st.set_page_config(page_title="Master Dashboard Page", page_icon =":material/drag_pan:")

#TitleDetails
st.title("Master Dashboard Page")
st.write ("This page links you to all home and business related dashboards.")
st.write("Use the encrypted entry code page in order to gain access to the credentials you need to enter.")


#Sidebar Links
st.sidebar.image("MHLogo_White.png.png")
st.sidebar.title("Dashboard Menu")
st.sidebar.page_link("MasterDashboard.py",label="Master Dashboard Page")
st.sidebar.page_link("pages/EntryCodes.py",label="Encrypted Entry Code Page")

#PageLinks

col1,col2 =st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Business Dashboard")
        st.write("This button leads you to the MH business dashboard, which contains updates regarding the business.")
        st.page_link("https://mhdashboardapp.streamlit.app/", label ="MH Dashboard",icon =":material/menu_book:",use_container_width=True, width="stretch")

with col2:
    with st.container(border=True):
        st.subheader("Home Dashboard")
        st.write("This button leads you to the home dashboard page, which contains updates regarding home grocery, meat and vegetable purchases. ")
        st.page_link("https://home-dashboard.streamlit.app/",label ="Home Dashboard",icon =":material/home:",use_container_width=True, width="stretch")

with st.container(border=True):
    st.subheader("Utility Dashboard")
    st.write("This button leads you to the utility monitoring dashboard, which contains updates regarding the cost and utilization of the following utilities: water, electricity, and solar energy.")
    st.page_link("https://utilitydashboard2026.streamlit.app/", label="Utility Dashboard", icon=":material/electric_bolt:",use_container_width=True, width="stretch")
