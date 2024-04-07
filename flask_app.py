from flask import Flask, request, jsonify
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

app = Flask(__name__)

## Function To get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q2_K.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    ## Prompt Template
    template = """{input_text}"""
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                            template=template)
    
    ## Generate the response from the LLama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

@app.route('/llm/generate_text', methods=['POST'])
def generate_blogs():
    data = request.get_json()
    input_text = data.get('input_text')
    no_words = data.get('no_words')
    blog_style = data.get('blog_style')
    response = getLLamaresponse(input_text, no_words, blog_style)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
