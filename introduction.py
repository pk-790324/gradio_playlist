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

#demo1.launch()


#Upload/Drop file with Gradio

def count_files(files):
    return f'Number of file uploaded: {len(files)}'

demo2=gr.Interface(
    fn=count_files,
    inputs=gr.File(file_count="multiple",
                   type='filepath',
                   label='Upload or Drag Files Here',
                   ),
    outputs=gr.Textbox(label='Number of Files Uploaded')
)

#demo2.launch()


#creating your first gradio interface 

def greet(name,intensity):
    return "Hello, " + name +'!'*int(intensity)

demo3=gr.Interface(
    fn=greet,
    inputs=['text','slider'],
    outputs=['text'],
    
)
#demo3.launch()


# gradio demo calculator

def add_number(number1,number2):
    return number1+number2

demo4=gr.Interface(
    fn=add_number,
    inputs=[gr.Number(),gr.Number()],
    outputs=gr.Number()
    
)
demo4.launch()