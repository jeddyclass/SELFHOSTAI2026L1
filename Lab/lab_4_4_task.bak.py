import gradio as gr
from agent_core import BusAssistantAgent
import time

# app.py

agent = BusAssistantAgent() # 初始化Agent，內部啟動Heartbeat

def respond(message, chat_history):
    # 1. 將使用者訊息送入Agent
    agent.receive_input(message)

    # 2. 等待Agent處理 (這裡需要一個非阻塞的機制來顯示Heartbeat)
    #    為了簡化，我們讓Agent的Heartbeat直接將訊息寫入一個全域佇列
    #    然後Gradio定期從這個佇列讀取並顯示。

    # 簡化版本：直接讓Agent同步處理完所有步驟 (失去即時性)
    # 更好的做法：使用 asyncio 或 websocket

    # 這裡示範一個簡化的同步版本
    response = agent.process_sync(message) # 同步處理，回傳最終結果
    chat_history.append((message, response))
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond_wrapper(message, chat_history):
        # 模擬Heartbeat的即時輸出 (實際上需要更複雜的機制)
        # 這裡我們只回傳最終結果
        return respond(message, chat_history)

    msg.submit(respond_wrapper, [msg, chatbot], [msg, chatbot])

demo.launch()
