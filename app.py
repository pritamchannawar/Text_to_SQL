from dotenv import load_dotenv # type: ignore
load_dotenv() #load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai # type: ignore

##configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Correcting the model name and response handling
def get_gemini_response(question, prompt):
    # Assuming the API expects a single string, concatenate prompt and question
    combined_input = prompt[0] + " " + question  # Concatenate the prompt and the question
    model = genai.GenerativeModel('gemini-pro')
    # Pass the combined string directly, without wrapping it into a list
    response = model.generate_content(combined_input)
    return response.text


# Corrected function for fetching rows from the database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()  # Corrected fetching of rows
    conn.close()  # Removed commit on a read operation
    return rows



prompt = [
    """
    Imagine yourself as an advanced SQL query generator with expertise in the healthcare domain. You have been provided with a SQL database named `hospital.db`, which contains tables called `PATIENTS`, `DOCTORS`, and `APPOINTMENTS`. The `PATIENTS` table includes the following columns: PATIENT_ID, NAME, AGE, GENDER, CONTACT_NUMBER, and ADDRESS. The `DOCTORS` table includes the following columns: DOCTOR_ID, NAME, SPECIALIZATION, and EXPERIENCE. The `APPOINTMENTS` table includes the following columns: APPOINTMENT_ID, PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, and TIME_SLOT. Your task is to translate English questions into precise SQL queries to retrieve information from these tables.

    For example,
    - If asked, "How many patients are registered in the database?", you should generate the SQL query: SELECT COUNT(*) FROM PATIENTS;
    - For a question like "Show me the details of female patients born after 1980," your SQL query should be: SELECT * FROM PATIENTS WHERE GENDER='F' AND AGE > 40;
    - If the question is, "Find all patients from 'Anytown' and their contact details," then produce the SQL command: SELECT NAME, CONTACT_NUMBER FROM PATIENTS WHERE ADDRESS='Anytown';

    Remember, your responses should directly translate the English inquiries into SQL commands without the use of code formatting symbols (like ```) at the beginning or end, nor should the word'sql' appear in your outputs. Aim to assist efficiently by converting complex questions into accurate SQL queries, enhancing data retrieval and analysis in the healthcare sector.
    """
]

##streamlit app

st.set_page_config(page_title = "I can retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL Query")

question= st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

# Revised streamlit display code
if submit:
    response = get_gemini_response(question, prompt)
    st.write(response)  # Using st.write() for display
    data = read_sql_query(response, "hospital.db")
    st.subheader("The response is:")
    for row in data:
        st.write(row)  # Displaying each row using st.write()