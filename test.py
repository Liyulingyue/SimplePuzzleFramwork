# 以utf8编码保存

import gradio as gr

with gr.Blocks() as demo:
    text1 = gr.Text()
    text2 = gr.Text()
    btn = gr.Button()

    btn.click(fn=lambda x: f"hello, {x}", inputs=text1, outputs=text2)

demo.launch()