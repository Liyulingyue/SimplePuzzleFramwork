from .gr_static import *
import gradio as gr
from ..LLM.ernie import ErnieClass
import os

ernie_access_token = os.environ["ERNIE_ACCESS_TOKEN"]
llm = ErnieClass(access_token=ernie_access_token)


def fn_text_place_change(text_place):
    return (gr.update(choices=objects[text_place], value="主体"),
            gr.update(value=[["展示信息", objects[text_place]["主体"]]]))

def fn_text_action(text_action, text_place, text_target, chatbot):
    if text_place!="家" or text_target!="椅子":
        return chatbot
    else:
        text_truth = "伙计在地下室挖了一个直通银行的密道，为了防止老板疑心，特意找理由将老板支走，最近终于大功告成，打算去银行偷黄金。"
        prompt = f"""
        用户的推理结果是；{text_action}, 
        案件的事实是：{text_truth}。
        请你判断用户是否正确推理。
        请你通过json的格式返回。
        返回内容是一个字典{"{"}"推理结果":int{"}"}。
        推理的正确，为1。推理的错误或者推理的完整度不高，为0。
        """
        result_dict = llm.get_llm_json_answer(prompt)
        print(result_dict)
        if result_dict["推理结果"]==1:
            chatbot.append([text_action, "推理正确！"])
        else:
            chatbot.append([text_action, "推理错误！"])
        return chatbot
