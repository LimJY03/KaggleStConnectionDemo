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

# Page header
st.title('KaggleStConnection Demo App')
st.markdown('---')

# Connect app to Kaggle API
conn = st.experimental_connection("kaggle", type=KaggleAPIConnection)

# Display user for current session
demo_col, docs_col = st.columns([3, 2])

cursor = conn.cursor()

with demo_col:
    current_user = cursor.get_config_value('username')
    st.success(f' Current Kaggle API Username: **{current_user}**')

with docs_col:

    st.write('''
             We can use the `cursor()` method to obtain the connection object. 
             In this case we use it to display the username of the API key.
             ''')

    st.write('''
             In practice, you should be using your own API key to connect to 
             the Kaggle API. The following quotes the steps to obtain your API 
             key on [**kaggle.com**](https://www.kaggle.com/) from the Kaggle 
             Documentation.
             ''')

    documentation.container(
        type='info',
        icon='🗨',
        head='''Kaggle\'s Public API Documentation 
                ([Read Here](https://www.kaggle.com/docs/api))''',
        info='''In order to use the Kaggle\'s public API, you must first 
                authenticate using an API token. Go to the \'Account\' tab of 
                your user profile and select \'Create New Token\'. This will 
                trigger the download of kaggle.json, a file containing your 
                API credentials.'''
    )

# Kaggle API info

# Demonstrate functions
sample_viz_tab, view_dataset_tab = st.tabs(
    ['Sample Visualization', 'Search and View Dataset File']
)

with sample_viz_tab:

    with st.expander('View dataframe'):

        st.write('''
                 We can use the `query()` method and specify the kaggle dataset
                 reference in the format of `\'[owner_slug]/[dataset_slug]\'` 
                 as the method argument.
                 ''')
        
        st.write('''
                 We can additionally use the `file` keyword argument where we 
                 can specify the dataset file to query from. By default, the
                 first file in the dataset will be queried.
                 ''')

        st.code('''
                # Using the previous initialized connection object `conn`
                data = conn.query(
                    'kritikseth/us-airbnb-open-data',   # Dataset ref
                    file='AB_US_2020.csv'               # Optional file to open
                )
                ''')

        st.markdown('---')

        data = conn.query(
            'kritikseth/us-airbnb-open-data',
            # file='AB_US_2020.csv'
        )

        num_rows = st.slider(
            'Number of rows to view',
            value=min(5, len(data)),
            min_value=1,
            max_value=min(100, len(data))
        )

        st.table(data.iloc[:num_rows])

    # Visualizations
    airbnb_visualization.show_3d_map(data)

with view_dataset_tab:

    documentation.container(
        type='warning',
        icon='🚧',
        head='Feature Under Development ...',
        info='''While waiting for this feature to complete developing, please 
                further explore this app and play around with other features'''
    )

    # st.table(data.iloc[:10])

    # # Choose dataset
    # search_input = st.text_input('Search a dataset', placeholder='Enter a word')

    # with st.form('search_dataset'):

    #     dataset_list_ref = []

    #     if search_input:

    #         dataset_lists = cursor.dataset_list(search=search_input, file_type='csv')
    #         dataset_list_ref = [data.ref for data in dataset_lists]

    #     user_select = st.selectbox('Select the dataset', dataset_list_ref)
    #     user_search = st.form_submit_button('Search')

    # if user_search:

    #     dataset_files = cursor.dataset_list_files(user_select)

    #     with st.form('select_file'):
    #         selected_file = st.selectbox('Select a dataset file', dataset_files.files)
    #         display_file = st.form_submit_button('Display')

    #     if display_file:

    #         data = conn.query(user_select, file=selected_file)
    #         st.table(data)
