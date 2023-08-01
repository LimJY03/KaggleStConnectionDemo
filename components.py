import streamlit as st

def info_box(info: str, head: str = '') -> st.info:

    return st.info(f'''**🗨 {head}**  
        {info}
    ''')