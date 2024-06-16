import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.MCQ_Generator.utils import read_file,get_table_data
import streamlit as st
from src.MCQ_Generator.mcqgenerator import generate_evaluate_chain
from src.MCQ_Generator.logger import logging


# loading json file
with open("./response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

#creating a title for the app
st.title("Questgen")
st.title("Mcq Generation Using Langchain⛓️🔗🦜")

# create a form using st.form
with st.form("user_inputs"):
    # File Upload
    uploaded_file = st.file_uploader("Upload a pdf or text file", type = ['pdf', 'txt'])

    #Input feilds
    mcq_count = st.number_input("No. of MCQ's", min_value=2, max_value=25)

    #Subject
    subject = st.text_input("Insert Subject", max_chars=20)

    #Quiz tone
    tone = st.text_input("Complexity Level of Questions", max_chars=20, placeholder="Simple")

    #Add button
    button = st.form_submit_button("Create MCQs")

    #Check if the button is clicked and has all inputs    

    if button and uploaded_file is not None and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                response=generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )
                #st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            # display the review in a text box as well
                            st.text_area(label = "Review", value=response['review'])
                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)







