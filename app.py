from KaggleAPIConnection import KaggleAPIConnection
import streamlit as st
import airbnb_visualization
import documentation

# Page config
st.set_page_config(
    page_title='KaggleStConnection Demo - Airbnb Distribution',
    page_icon=':house_with_garden:',
    layout='wide',
)

# Connect app to Kaggle API
conn = st.experimental_connection("kaggle", type=KaggleAPIConnection)
cursor = conn.cursor()

# Page header
st.title('KaggleStConnection Demo App')
st.markdown('---')

# Connection description
st.write('''
         **KaggleStConnection** is a Streamlit connection class that connects to Kaggle
         API. Better than the default [Kaggle API](https://www.kaggle.com/docs/api), 
         **KaggleStConnection** automates the reading of a specific data file from 
         your desired dataset found on Kaggle.
         ''')

st.write('''
         You can view the source GitHub repository for the connection class and the
         demo app in the links below:
         * [KaggleStConnection](https://github.com/genesis331/KaggleStConnection)
         * [KaggleStConnectionDemo](https://github.com/LimJY03/KaggleStConnectionDemo)
         ''')

with st.expander('View **KaggleStConnection** documentation'):
    documentation.main_docs()

# Demonstrate functions
sample_viz_tab, view_connection_info = st.tabs(
    ['Sample Visualization', 'View Connection Info']
)

with sample_viz_tab:
    airbnb_visualization.run(conn)

with view_connection_info:

    # Display user for current session
    current_user = cursor.get_config_value('username')

    st.success(f' Current Kaggle API Username: **{current_user}**')
    # st.toast(':white_check_mark: **Connection Success**')

    st.write('''
             We can use the `cursor()` method to obtain the connection object. 
             In this case we use it to display the username of the API key.
             ''')

    st.code('''
            # Get cursor object
            cursor = conn.cursor()

            # Get API username
            current_user = cursor.get_config_value('username')
            ''')

    st.write('''
             In practice, you should be using your own API key to connect to 
             the Kaggle API. Read more about it in the documentation expander
             above.
             ''')
