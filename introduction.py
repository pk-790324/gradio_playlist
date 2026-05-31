import gradio as gr

def sum(a,b):
    a=input('enter first number')
    b=input('enter second number')
    print('the sum of a and b is :',a+b)

def process_text(text):
    return f"You enterd: '{text}'"

demo=gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label='enter some text'),
    outputs=gr.Textbox(label='output')
)

demo.launch()