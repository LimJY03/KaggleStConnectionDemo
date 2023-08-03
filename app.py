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
documentation.container(
    type='warning',
    icon='🚧',
    head='Description Under Development ...',
    info='''While waiting for this description to complete developing, 
            please further explore this app and play around with other features
            '''
)

st.write('''
         :orange[// Lorem ipsum description undone gg]
         ''')

st.write('''
         :orange[// Reference to API repo and Demo repo more lorem ipsum undone gg]
         ''')

st.write('''
         :orange[// Dependency lists & how to setup]
         ''')

# Demonstrate functions
sample_viz_tab, view_dataset_tab, view_connection_info = st.tabs(
    ['Sample Visualization', 'Search and View Dataset File', 'View Connection Info']
)

with sample_viz_tab:

    st.write('''
             We are using the \'AB_US_2023.csv\' data file from the 
             [**US Airbnb Open Data**](https://www.kaggle.com/dataset/kritikseth/us-airbnb-open-data) 
             dataset by Kritikseth for this sample visualization. You may 
             expand the \'View dataframe\' expander to see the top $N$ rows in 
             this dataframe.
             ''')

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
                    file='AB_US_2023.csv'               # Optional file to open
                )
                ''')
        
        st.write('''
                 In this case, we set the parameter `file` to `\'AB_US_2023.csv\'` 
                 so that we will obtain the desired latest data for our sample
                 visualization. 
                 ''')

        st.markdown('---')

        data = conn.query(
            'kritikseth/us-airbnb-open-data',
            file='AB_US_2023.csv'
        )

        num_rows = st.slider(
            'Number of rows to view',
            key='sample_viz_tab',
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
        head='Description Under Development ...',
        info='''While waiting for this description to complete developing, 
                please further explore this app and play around with other 
                features'''
    )

    # Choose dataset
    search_input = st.text_input('Search a dataset', placeholder='Enter a word')

    # dataset_list_ref = []

    if search_input:

        dataset_lists = cursor.dataset_list(search=search_input, file_type='csv')
        dataset_list_ref = [data.ref for data in dataset_lists]
        user_select = st.selectbox('Select the dataset', dataset_list_ref)

        if user_select:

            dataset_files = cursor.dataset_list_files(user_select)
            selected_file = st.selectbox('Select a dataset file', dataset_files.files)

            if selected_file:

                selected_data = conn.query(user_select, file=selected_file)

                num_rows = st.slider(
                    'Number of rows to view',
                    key='view_dataset_tab',
                    value=min(5, len(selected_data)),
                    min_value=1,
                    max_value=min(100, len(selected_data))
                )

                st.table(selected_data.iloc[:num_rows])

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

    st.write('''
             To use your API keys in streamlit, you can either:
             * Go to your **Project Root (~)** and create a 
             ''')

    # Kaggle API info
