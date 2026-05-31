import gradio as gr

def process_text(text):
    return f"You enterd: '{text}'"

demo=gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label='enter some text'),
    outputs=gr.Textbox(label='output')
)

# demo.launch()


#multiple inputs with gradio

def process_text_and_number(text,number):
    return f"the text is '{text}' and number is {number}"

demo1=gr.Interface(
    fn=process_text_and_number,
    inputs=[
        gr.Textbox(label="Enter the Text "),
        gr.Number(label="Enter the number")
    ],
    outputs=gr.Textbox(label='Output')
    
)

demo1.launch()