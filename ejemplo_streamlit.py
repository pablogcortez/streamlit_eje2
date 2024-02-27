import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Step 2: Load configuration file and create authentication object
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Step 2: Render login widget
authenticator.login()

# Step 3: Authenticating users
if st.session_state["authentication_status"]:
    authenticator.logout()  # Optionally logout user
    st.write(f'Welcome {st.session_state["name"]}')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
