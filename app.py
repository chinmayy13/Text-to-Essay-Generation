import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Fucntion to get response from LLAMA 2 Model

def responsefromLLAMA2Model(input_text, blog_for,no_words):
    llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,'temperature':0.01})
    
    ## Prompt template
    template= """
    Write an Essay for {blog_for} job profile for a topic of {input_text} and make sure to keep 
    word limits upto {no_words}.
    
    
    """
    
    prompt=PromptTemplate( input_variables=['blog_for','input_text','no_words'],template=template)
    
    ## Generate Response from llama 2 Model
    response =llm(prompt.format(blog_for=blog_for,input_text=input_text,no_words=no_words))
    print(response)
    return response
    
     












st.set_page_config(page_title='Essay Writer',
                  page_icon='😎',
                  layout='centered',
                  initial_sidebar_state='collapsed')

st.header('Generate Essays 😏')

input_text= st.text_input("Enter the Topic Name🤔")

## Creating additional fields
col1,col2= st.columns([5,5])

with col1:
    no_words=st.text_input('Number of Words')
with col2:
    blog_for= st.selectbox('Writing the Essay for' ,('Student','Researcher', 'Professional','Kid'),index=0)

submit=st.button("Generate 🤩")


if submit:
    st.write(responsefromLLAMA2Model(input_text, blog_for,no_words))