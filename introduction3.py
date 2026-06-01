
import gradio as gr
 
import ollama
 
 
 
def chatbot(text):
    response=ollama.generate(model='tinyllama:1.1b',prompt='text')
    return response['response']
   
   
   
   
demo=gr.Interface(
    fn=chatbot,
    inputs=['text'],
    outputs=['text']
)
demo.launch()