# import streamlit as st

# from vanna.remote import VannaDefault

# @st.cache_resource(ttl=3600)
# def setup_vanna():
#     vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='chinook')
#     vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
#     return vn

# @st.cache_data(show_spinner="Generating sample questions ...")
# def generate_questions_cached():
#     vn = setup_vanna()
#     return vn.generate_questions()


# @st.cache_data(show_spinner="Generating SQL query ...")
# def generate_sql_cached(question: str):
#     vn = setup_vanna()
#     return vn.generate_sql(question=question, allow_llm_to_see_data=True)

# @st.cache_data(show_spinner="Checking for valid SQL ...")
# def is_sql_valid_cached(sql: str):
#     vn = setup_vanna()
#     return vn.is_sql_valid(sql=sql)

# @st.cache_data(show_spinner="Running SQL query ...")
# def run_sql_cached(sql: str):
#     vn = setup_vanna()
#     return vn.run_sql(sql=sql)

# @st.cache_data(show_spinner="Checking if we should generate a chart ...")
# def should_generate_chart_cached(question, sql, df):
#     vn = setup_vanna()
#     return vn.should_generate_chart(df=df)

# @st.cache_data(show_spinner="Generating Plotly code ...")
# def generate_plotly_code_cached(question, sql, df):
#     vn = setup_vanna()
#     code = vn.generate_plotly_code(question=question, sql=sql, df=df)
#     return code


# @st.cache_data(show_spinner="Running Plotly code ...")
# def generate_plot_cached(code, df):
#     vn = setup_vanna()
#     return vn.get_plotly_figure(plotly_code=code, df=df)


# @st.cache_data(show_spinner="Generating followup questions ...")
# def generate_followup_cached(question, sql, df):
#     vn = setup_vanna()
#     return vn.generate_followup_questions(question=question, sql=sql, df=df)

# @st.cache_data(show_spinner="Generating summary ...")
# def generate_summary_cached(question, df):
#     vn = setup_vanna()
#     return vn.generate_summary(question=question, df=df)



import streamlit as st
from vanna.remote import VannaDefault

# Cache the Vanna setup to avoid reinitializing it frequently
@st.cache_resource(ttl=3600)
def setup_vanna():
    # Initialize Vanna with the API key and model name
    vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='chinook')
    # Connect to the SQLite database
    vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
    return vn

# Cache the generation of sample questions to improve performance
@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached():
    vn = setup_vanna()
    # Generate and return sample questions
    return vn.generate_questions()

# Cache the generation of SQL queries
@st.cache_data(show_spinner="Generating SQL query ...")
def generate_sql_cached(question: str):
    vn = setup_vanna()
    # Generate SQL for the given question, allowing the LLM to see the data
    return vn.generate_sql(question=question, allow_llm_to_see_data=True)

# Cache the validation of SQL queries
@st.cache_data(show_spinner="Checking for valid SQL ...")
def is_sql_valid_cached(sql: str):
    vn = setup_vanna()
    # Check if the SQL query is valid
    return vn.is_sql_valid(sql=sql)

# Cache the execution of SQL queries
@st.cache_data(show_spinner="Running SQL query ...")
def run_sql_cached(sql: str):
    vn = setup_vanna()
    # Run the SQL query and return the results
    return vn.run_sql(sql=sql)

# Cache the decision on whether to generate a chart
@st.cache_data(show_spinner="Checking if we should generate a chart ...")
def should_generate_chart_cached(question, sql, df):
    vn = setup_vanna()
    # Determine if a chart should be generated based on the data
    return vn.should_generate_chart(df=df)

# Cache the generation of Plotly code for charts
@st.cache_data(show_spinner="Generating Plotly code ...")
def generate_plotly_code_cached(question, sql, df):
    vn = setup_vanna()
    # Generate Plotly code for the chart based on the question and data
    code = vn.generate_plotly_code(question=question, sql=sql, df=df)
    return code

# Cache the generation of Plotly figures
@st.cache_data(show_spinner="Running Plotly code ...")
def generate_plot_cached(code, df):
    vn = setup_vanna()
    # Generate and return the Plotly figure using the provided code and data
    return vn.get_plotly_figure(plotly_code=code, df=df)

# Cache the generation of follow-up questions
@st.cache_data(show_spinner="Generating followup questions ...")
def generate_followup_cached(question, sql, df):
    vn = setup_vanna()
    # Generate follow-up questions based on the original question and results
    return vn.generate_followup_questions(question=question, sql=sql, df=df)

# Cache the generation of a summary of the results
@st.cache_data(show_spinner="Generating summary ...")
def generate_summary_cached(question, df):
    vn = setup_vanna()
    # Generate a summary of the results based on the question and data
    return vn.generate_summary(question=question, df=df)