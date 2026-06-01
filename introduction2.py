import gradio as gr

def sentence_builder(quantity,tech_worker_type,countries,place,activity_list,morning):
    return f"""The {quantity} {tech_worker_type}s from {' and '.join(countries)} went to the {place} where they {' and '.join(activity_list)} until the {'morning' if morning else 'night'}"""


demo=gr.Interface(
    fn=sentence_builder,
    inputs=[gr.Slider(3,20,step=1,label='cont',info='choose between 3 and 20'),
            gr.Dropdown(
                ['Data Scientist','Software Developer','Software Engineer'],
                label='Tech Wroker Type',
                info='will add more tech worker types later!'
            ),
            gr.CheckboxGroup(['Canada','Japan','France'],label='Countries',info='Where are they from?'),
            gr.Radio(['Office','Restaurant','Meeting room'],label='location',info='Where did they go?'),
            gr.Dropdown(['Partied','Brainstormed','coded','Fixed bugs'],
                        value=['Brainstormed','Fixed bugs'],
                        multiselect=True,
                        label='Activities',
                        info='Which activites did they perform?'
                        ),
            gr.Checkbox(label='Morning',info='Did they do it in morning?')
            ],
    outputs='text',
    examples=[
        [3, "Software Developer", ["Canada", "Japan"], "Restaurant", ["coded", "fixed bugs"], True],
        [4, "Data Scientist", ["Japan"], "Office", ["Brainstormed", "Partied"], False],
        [10, "Software Engineer", ["Canada", "France"], "Meeting room", ["Brainstormed"], False],
        [8, "Data Scientist", ["France"], "Restaurant", ["coded"], True],
    ]
    
)

demo.launch()