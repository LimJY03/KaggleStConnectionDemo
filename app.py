import streamlit as st
import components
from KaggleAPIConnection import KaggleAPIConnection

# Page config
st.set_page_config(
    page_title='KaggleStConnection Demo - Airbnb Distribution',
    page_icon='🏡',
    layout='wide',
)

# Page header
st.title('AirBnb Distribution Demo')
st.markdown('---')

# Connect app to Kaggle API
conn = st.experimental_connection("kaggle", type=KaggleAPIConnection)

# Display user for current session
cursor = conn.cursor()
current_user = cursor.get_config_value('username')
st.write('After connection to Kaggle API is successful, the below green box will appear')
st.success(f' Your Kaggle API Username: **{current_user}**')
st.toast('**Connection Successful!!**', icon='✅')

# Kaggle API info
st.write('In practice, you should be using your own API key to connect to the Kaggle API. The following quotes the steps to obtain your API key on [**kaggle.com**](https://www.kaggle.com/) from the Kaggle Documentation.')
components.info_box(head='Kaggle\'s Public API Documentation ([Read Here](https://www.kaggle.com/docs/api))',
                    info='In order to use the Kaggle\'s public API, you must first authenticate using an API token. Go to the \'Account\' tab of your user profile and select \'Create New Token\'. This will trigger the download of kaggle.json, a file containing your API credentials.')

# Preview data
st.write('Below we query the first 10 rows of [**kamilenovaes/global-blood-type-distribution**](https://www.kaggle.com/datasets/kamilenovaes/global-blood-type-distribution) dataset from kaggle using our KaggleStConnection connector')
data = conn.query('kamilenovaes/global-blood-type-distribution')

st.table(data.iloc[:10])

# # Choose dataset
# search_input = st.text_input('Search a dataset', placeholder='Enter a word')

# with st.form('search_dataset'):

#     dataset_list = []

#     if search_input:

#         dataset_lists = cursor.dataset_list(search=search_input, file_type='csv')
#         dataset_list = [data.ref for data in dataset_lists]

#     user_select = st.selectbox('Select the dataset', dataset_list)

#     user_search = st.form_submit_button('Search')

# print(type(user_select))

# if user_search:

#     data = conn.query(user_select)
#     st.table(data)
