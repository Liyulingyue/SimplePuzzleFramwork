import gradio as gr
from .gr_static import *
from .gr_functions import *

with gr.Blocks() as demo:
    gr.Markdown(title_text)
    with gr.Row():
        img = gr.Image(label=img_title, value="Source/Map.jpg", interactive=False)
        with gr.Column():
            text_system = gr.Textbox(label="系统提示框")
            text_place = gr.Dropdown(label="请选择地点", choices=objects, value="家", interactive=True)
            text_target = gr.Dropdown(label="请选择目标", choices=objects[text_place.value], value="主体", interactive=True)
            with gr.Row():
                text_action = gr.Textbox(label="请输入你想要进行的动作和行为", interactive=True, scale=3)
                btn_send = gr.Button(value="发送", scale=1)
            chatbot = gr.Chatbot(label="对话记录", value=[["展示信息", objects[text_place.value][text_target.value]]])
    btn_start = gr.Button(value="开始游戏，目前这个按钮没什么用")

    text_place.change(fn=fn_text_place_change, # lambda x: gr.update(choices=objects[x], value="主体"),
                      inputs=text_place,
                      outputs=[text_target, chatbot])
    text_target.change(fn=lambda x,y: gr.update(value=[["展示信息", objects[x][y]]]),
                       inputs=[text_place, text_target],
                       outputs=chatbot)
    btn_send.click(fn=fn_text_action,
                   inputs=[text_action, text_place, text_target, chatbot],
                   outputs=chatbot)