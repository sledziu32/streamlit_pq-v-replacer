import streamlit as st
from jinja2 import Template
import pandas as pd

st.set_page_config(
    page_title="PowerQuery chained text replace generator",
    page_icon="💻",
    layout="wide")




st.title("PowerQuery chained text replace generator")

"---"
x1,c1, c2,x2 =st.columns((3,2,2,3))
with c1:
    st.text_input("Previous step", value="step", key="pre")
    st.text_input("Column name", value="column", key="col")


"---"

@st.cache_data
def load_data():
    data = {
        "old_text": [],
        "new_text": []
    }
    df = pd.DataFrame(data)
    df["old_text"] = df["old_text"].astype("str")
    df["new_text"] = df["new_text"].astype("str")
    
    return df


def create_pq( state = st.session_state):
    pre = f'#"{state["pre"]}"'
    col = state["col"]
    rows = state["data_editor"]["added_rows"]
    
    query = pre
    
    if len(rows) == 0:
        return ""
    else:
        for i in rows:
            try:
                query = 'Table.ReplaceValue( '+query+ ', "'+i["old_text"]+'", "'+i["new_text"]+ '", Replacer.ReplaceText,{"'+col+'"})'
            except:
                pass
        return f"""= {query}"""
        

df = load_data()

with c2:
    st.data_editor(df, key="data_editor", num_rows="dynamic")

st.write("your query:")
st.code(create_pq())
# st.write("Here's the session state:")
# ar = st.session_state["data_editor"]["added_rows"]
# ar
# st.write(len(ar))

# "= Table.ReplaceValue(#"Zmieniono typ","aa","bb",Replacer.ReplaceText,{"Kolumna 1"})"

