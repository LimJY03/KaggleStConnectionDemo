from kaggle import KaggleApi
import streamlit as st
import documentation

def run(conn: st.experimental_connection, cursor: KaggleApi) -> None:
    '''
    Executes the dataset search feature
    
    '''

    st.write('''
             Here we can view the list off datasets with `.csv` data files from
             Kaggle. You can enter some words in the search box below and it will
             display a dropdown for you to select your desired dataset.
             ''')

    # Choose dataset
    search_input = st.text_input(
        'Search a dataset', 
        value='global blood',
        # placeholder='Enter a word'
    )

    # Search dataset
    if search_input:

        st.write('''
                 To return the list of datasets related to the search box, we used
                 the `dataset_list` method from `KaggleAPI` by calling it from our
                 `cursor` object. The sample code to do this is shown below.
                 ''')
        
        st.code('''
                # Get cursor object
                cursor = conn.cursor()

                # Search dataset
                datasets = cursor.dataset_list(search=user_input, file_type='csv')
                ''')
        
        st.write('''
                 Usually, we will be using the same `cursor` object throughout the
                 whole program, but for the sake of explanation we will specify it
                 in the code block above.
                 ''')

        dataset_lists = cursor.dataset_list(search=search_input, file_type='csv')

        # Select desired dataset
        if dataset_lists:

            dataset_list_ref = [data.ref for data in dataset_lists]
            user_select = st.selectbox('Select the dataset', dataset_list_ref)

            # Select dataset file
            if user_select:

                dataset_files = cursor.dataset_list_files(user_select)

                # Check if dataset has files
                if dataset_files.files:

                    selected_file = st.selectbox('Select a dataset file',
                                                 sorted(map(str, dataset_files.files)))

                    # Query selected dataset file
                    if selected_file:

                        selected_data = conn.query(user_select, ttl=1, file=selected_file)

                        # Display logic
                        if len(selected_data.index) > 1:

                            num_rows = st.slider(
                                'Number of rows to view',
                                key='view_dataset_tab',
                                value=min(5, len(selected_data)),
                                min_value=1,
                                max_value=min(100, len(selected_data))
                            )

                            st.table(selected_data.iloc[:num_rows])

                        else: st.table(selected_data)

                else:
                    documentation.container(
                        ctype='warning',
                        icon='⚠',
                        head='No Files In Dataset',
                        info='''Try searching for other datasets here or at the official
                                [Kaggle Website](https://www.kaggle.com/datasets/).
                                '''
                    )

        else: 
            documentation.container(
                ctype='warning',
                icon='⚠',
                head='Dataset Not Found',
                info='''Try searching for other datasets here or at the official
                        [Kaggle Website](https://www.kaggle.com/datasets/).
                        '''
            )