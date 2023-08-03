import streamlit as st

def container(info: str, head: str = '', icon: str = '', ctype: str = 'info') -> st.info:
    '''
    Reusable container with optional icon and heading
    - Color depends on `ctype` param
        - info -> blue
        - warning -> yellow
        - error -> red
    '''

    return exec(f"""st.{ctype}(f'''**{icon} {head}**  
        {info}
    ''')""")

def main_docs() -> None:
    '''Writes the documentation for KaggleStConnection'''

    st.markdown('### Package Installation')
    
    st.write('''
            To install **KaggleStConnection** in your local machine, just install 
            the package with the code below in the terminal and you are ready to 
            go.
            ''')

    st.code('''
            pip install git+https://github.com/genesis331/KaggleStConnection.git@v1.2.2
            ''',
            language='sh')
    
    st.markdown('### Initializing KaggleStConnection')

    st.write('''
             After you have installed the **KaggleStConnection** package
             in the step above, you can start to initialize a connection to the 
             Kaggle API and obtain a connection object with the following code. 
             ''')
    
    st.code('''
            # Initialize connection
            conn = st.experimental_connection("kaggle", type=KaggleAPIConnection)

            # Obtain connection object
            cursor = conn.cursor()
            ''')

    st.write('''
             You can use the connection object `cursor` to call some KaggleAPI 
             methods like `dataset_list()` and many more depending on your use
             cases.
             ''')

    st.markdown('### Querying Data From Kaggle Datasets')

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
             visualization shown below. 
             ''')
    
    st.markdown('### Configuring Kaggle API Key')

    st.write('''
             Before the above code can work, we will need to specify the API
             key during the initialization of the connection. The following 
             quotes the steps to obtain your API key on 
             [kaggle.com](https://www.kaggle.com/) from the Kaggle 
             Documentation.
             ''')
    
    container(
        ctype='info',
        icon='🗨',
        head='''Kaggle\'s Public API Documentation 
                ([Read Here](https://www.kaggle.com/docs/api))''',
        info='''In order to use the Kaggle\'s public API, you must first 
                authenticate using an API token. Go to the \'Account\' tab of 
                your user profile and select \'Create New Token\'. This will 
                trigger the download of `kaggle.json`, a file containing your 
                API credentials.'''
    )

    st.write('''
             To use your API keys in streamlit, you can either:
             * Go to your **Project Root (~)** and create a `.kaggle` folder
             and place your `kaggle.json` inside the folder.
             * Go to your **Workspace Root** and create a `.streamlit` folder
             and create a `secrets.toml` file, then enter the following in the
             file:
                ```toml
                [connections.kaggle]
                kaggle_username='<USERNAME>'
                kaggle_key='<API_KEY>'
                ```
                Replace the `<USERNAME>` and the `<API_KEY>` with that in your
                `kaggle.json` file.  
             * :red[**[NOT RECOMMENDED FOR PUBLIC DEPLOYMENT]**] 
                Specify the `kaggle_username` and `kaggle_key` optional parameter 
                during the initialization of the connection with 
                `st.experimental_connection`. An example of this usecase is shown 
                as below:
                ```py
                conn = st.experimental_connection(
                    'kaggle', 
                    type=KaggleAPIConnection,
                    kaggle_username='<USERNAME>',
                    kaggle_key='<API_KEY>'
                )
                ```
                Similarly as the previous bullet, replace the `<USERNAME>` and 
                the `<API_KEY>` with that in your `kaggle.json` file. 
             ''')

    st.write('''
             You can read more about secrets management in the 
             [Streamlit's secrets management documentations](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management).
             ''')