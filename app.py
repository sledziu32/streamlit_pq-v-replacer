import streamlit as st
import pandas as pd


_about = """
## About This App

Welcome to the PowerQuery chained text replace generator!
This Streamlit app is designed to make your data transformation tasks easier. It allows you to generate PowerQuery statements from the data you insert, creating chained text replace queries effortlessly.
### How it Works

1. **Insert Data:** Begin by providing the data you want to transform. 
2. **Copy and Use:** Simply copy it and integrate it into your data workflow. Watch as your data is transformed efficiently.
### Why Use PowerQuery?
PowerQuery is a powerful tool for data transformation in various applications, including Excel and Power BI. It allows you to clean, shape, and enrich your data easily, making it an essential tool for data professionals.
Whether you're a data analyst, a business intelligence professional, or someone looking to streamline their data processing tasks, this app will simplify the process for you.
Feel free to explore and enjoy the benefits of automated PowerQuery statement generation. If you have any questions or feedback, don't hesitate to reach out.

Happy data transforming!


[Przemysław Zawadzki](https://www.linkedin.com/in/przemyslawzawadzki/)

**DataBase Analyst**

Project Management Office

IRIS Telecommunication Poland Sp. z o.o. 

![](https://www.iris-telecommunication.pl/sites/all/themes/awesomeit/img/logo2.jpg)
"""

st.set_page_config(
    page_title="PowerQuery chained text replace generator",
    page_icon="💻",
    layout="wide",
    menu_items={'About': _about})




st.title("PowerQuery chained text replace generator")

"---"
x1,c1, c2,x2 =st.columns((3,2,3,2),)
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
    "insert data to table below (you can paste them from spreadsheet)"
    
    st.data_editor(df, key="data_editor", num_rows="dynamic")

st.write("your query:")
st.code(create_pq(), language="powerquery")


