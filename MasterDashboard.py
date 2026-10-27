import streamlit as st

st.set_page_config(page_title="Master Dashboard Page", page_icon =":material/drag_pan:")


# Load credentials securely from .streamlit/secrets.toml
USER_CREDENTIALS = st.secrets["password"]

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False


def login():
    # Hide the sidebar completely when on the login screen
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🔒 Master Dashboard Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Sign In")

        if submit:
            # Strip spaces just in case of accidental auto-correct spacing
            clean_user = username.strip()
            clean_pass = password.strip()

            # Directly check against your st.secrets keys
            if clean_user == st.secrets["username"] and clean_pass == st.secrets["password"]:
                st.session_state["authenticated"] = True
                st.session_state["username"] = clean_user
                st.rerun()
            else:
                st.error("Invalid Username or Password")


if not st.session_state["authenticated"]:
    login()
    st.stop()


#TitleDetails
st.title("Master Dashboard Page")
st.write ("This page links you to all home and business related dashboards.")
st.write("Use the encrypted entry code page in order to gain access to the credentials you need to enter.")


#Sidebar Links
st.sidebar.image("MHLogo_White.png.png")
st.sidebar.title("Dashboard Menu")
st.sidebar.page_link("MasterDashboard.py",label="Master Dashboard Page")
st.sidebar.page_link("pages/EntryCodes.py",label="Encrypted Entry Code Page")

st.sidebar.markdown("---")
if st.sidebar.button("Logout"):
    st.session_state["authenticated"] = False
    st.rerun()






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
