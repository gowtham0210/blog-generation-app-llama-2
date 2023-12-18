import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


##Function to get response from LLAMA 2 model
def getllamaresponse(input_text,num_words,blog_style):
    #LLAMA 2 Model importing
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})

    #Prompt Template
    template = '''
        write a blog for {blog_style} job profile for a topic {input_text} 
        within {num_words} words.
    '''

    prompt = PromptTemplate(input_variables=["blog_style","input_text","num_words"],template=template)

    #Generate response from the LLAMA 2 model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,num_words=num_words))
    print(response)
    return response




st.set_page_config(page_title="Blog Generation APP",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header('Generate Blogs')

input_text = st.text_input("Enter the Blog Topic")

##Creating 2 columns for getting input field
#col1-get the no of words
#col2-get the style of input

col1,col2 = st.columns([5,5])

with col1:
    num_words = st.text_input('No of words')

with col2:
    blog_style = st.selectbox('write the Blog for',('Researchers','Data Scientist','Common People'),index=0)

submit = st.button("Generate")

#Final Response
if submit:
    st.write(getllamaresponse(input_text,num_words,blog_style))