import streamlit as st

# 1. Page Configuration (Must always be the first Streamlit command)
st.set_page_config(page_title="Master Dashboard Page", page_icon=":material/drag_pan:")

# 2. Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 3. Define the Login Page View
def show_login_page():
    st.title("🔒 Master Dashboard Login")
    st.write("Please enter your credentials to access the master dashboard.")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Log In")
        
        if submit_button:
            # Strip accidental leading/trailing whitespace
            clean_user = username.strip()
            clean_pass = password.strip()
            
            # Replace with your actual credentials or st.secrets
            expected_user = "admin"
            expected_pass = "your_secure_password"  # Make sure this matches what you're typing!
            
            if clean_user == expected_user and clean_pass == expected_pass:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Invalid username or password. Please try again.")

# 4. Control Access Based on Authentication Status
if not st.session_state["authenticated"]:
    show_login_page()
else:
    # --- YOUR ORIGINAL DASHBOARD CODE ---
    
    # Add a Log Out option in the sidebar
    if st.sidebar.button("Log Out", icon=":material/logout:"):
        st.session_state["authenticated"] = False
        st.rerun()

    # Title Details
    st.title("Master Dashboard Page")
    st.write("This page links you to all home and business related dashboards.")
    st.write("Use the encrypted entry code page in order to gain access to the credentials you need to enter.")

    # Sidebar Links
    st.sidebar.image("MHLogo_White.png.png")
    st.sidebar.title("Dashboard Menu")
    st.sidebar.page_link("MasterDashboard.py", label="Master Dashboard Page")
    st.sidebar.page_link("pages/EntryCodes.py", label="Encrypted Entry Code Page")

    # Page Links
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Business Dashboard")
            st.write("This button leads you to the MH business dashboard, which contains updates regarding the business.")
            st.page_link("https://mhdashboardapp.streamlit.app/", label="MH Dashboard", icon=":material/menu_book:", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("Home Dashboard")
            st.write("This button leads you to the home dashboard page, which contains updates regarding home grocery, meat and vegetable purchases.")
            st.page_link("https://home-dashboard.streamlit.app/", label="Home Dashboard", icon=":material/home:", use_container_width=True)

    with st.container(border=True):
        st.subheader("Utility Dashboard")
        st.write("This button leads you to the utility monitoring dashboard, which contains updates regarding the cost and utilization of the following utilities: water, electricity, and solar energy.")
        st.page_link("https://utilitydashboard2026.streamlit.app/", label="Utility Dashboard", icon=":material/electric_bolt:", use_container_width=True)

