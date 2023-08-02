import streamlit as st

def container(info: str, head: str = '', icon: str = '', type: str = 'info') -> st.info:

    return exec(f"""st.{type}(f'''**{icon} {head}**  
        {info}
    ''')""")