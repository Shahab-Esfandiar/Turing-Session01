# main.py
import os
import gradio as gr
import pandas as pd

from infra.llm.factory import ClientFactory
from app.use_cases.summarizer import Summarizer
from app.use_cases.classifier import TextClassifier
from app.use_cases.translator import Translator
from core.exceptions import AIAppError
from core.logger import logger

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "app/prompts")

def load_template(filename):
    path = os.path.join(PROMPT_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# -------- Handlers --------
def handle_sum(text, provider, local_model, prompt_file):
    try:
        if not text.strip(): return "Empty Input"
        model_to_use = local_model if provider == "Ollama" else None
        client = ClientFactory.get_client(provider, specific_model=model_to_use)
        service = Summarizer(client)
        template = load_template(prompt_file)
        res, time = service.summarize(text, template)
        return f"{res}\n\n⏱ Est. Reading Time: {time}s"
    except AIAppError as e:
        logger.error(f"UI Error in Summarization: {e}")
        return f"Service Error: {str(e)}"

def handle_cls(text, provider, local_model, prompt_file):
    try:
        if not text.strip(): return "Empty Input"
        model_to_use = local_model if provider == "Ollama" else None
        client = ClientFactory.get_client(provider, specific_model=model_to_use)
        service = TextClassifier(client)
        template = load_template(prompt_file)
        return service.classify(text, template)
    except AIAppError as e:
        logger.error(f"UI Error in Classification: {e}")
        return f"Service Error: {str(e)}"

def handle_tra(text, provider, local_model, src, tgt, tone):
    try:
        if not text.strip(): return "Empty Input"
        model_to_use = local_model if provider == "Ollama" else None
        client = ClientFactory.get_client(provider, specific_model=model_to_use)
        service = Translator(client)
        filename = f"translation_{tone.lower()}.txt"
        template = load_template(filename)
        return service.translate(text, src, tgt, tone, template)
    except AIAppError as e:
        logger.error(f"UI Error in Translation: {e}")
        return f"Service Error: {str(e)}"

# -------- Flagging Wrappers --------
def flag_sum(*args):
    sum_callback.flag(list(args))

def flag_cls(*args):
    cls_callback.flag(list(args))

def flag_tra(*args):
    tra_callback.flag(list(args))

# -------- UI Layout --------
all_files = [f for f in os.listdir(PROMPT_DIR) if f.endswith(".txt")]
ollama_models = ["gemma3:4b", "llama3.1:8b"]

sum_callback = gr.CSVLogger()
cls_callback = gr.CSVLogger()
tra_callback = gr.CSVLogger()

with gr.Blocks(title="AI Text Engine v2") as demo:
    gr.Markdown("# 🚀 AI Text Engine v2")

    with gr.Tabs():

        # Summarization Tab
        with gr.Tab("Summarization"):
            with gr.Row():
                with gr.Column():
                    si = gr.Textbox(lines=8, label="Input Text")
                    with gr.Row():
                        sm = gr.Dropdown(["OpenAI", "Ollama"], value="Ollama", label="Provider")
                        sl = gr.Dropdown(ollama_models, value="gemma3:4b", label="Local Model")
                    sp = gr.Dropdown([p for p in all_files if "summarization" in p], label="Template")
                    with gr.Row():
                        sb = gr.Button("Summarize", variant="primary")
                        sf = gr.Button("🚩 Flag Result")
                so = gr.Textbox(lines=10, label="Result")
            
            sb.click(handle_sum, inputs=[si, sm, sl, sp], outputs=so)
            sum_callback.setup([si, sm, sl, sp, so], "flagged_summarization")
            sf.click(flag_sum, inputs=[si, sm, sl, sp, so], outputs=None)

        # Classification Tab
        with gr.Tab("Classification"):
            with gr.Row():
                with gr.Column():
                    ci = gr.Textbox(lines=8, label="Input Text")
                    with gr.Row():
                        cm = gr.Dropdown(["OpenAI", "Ollama"], value="Ollama", label="Provider")
                        cl = gr.Dropdown(ollama_models, value="gemma3:4b", label="Local Model")
                    cp = gr.Dropdown([p for p in all_files if "classification" in p], label="Template")
                    with gr.Row():
                        cb = gr.Button("Analyze", variant="primary")
                        cf = gr.Button("🚩 Flag Result")
                co = gr.Textbox(label="Category & Confidence")
            
            cb.click(handle_cls, inputs=[ci, cm, cl, cp], outputs=co)
            cls_callback.setup([ci, cm, cl, cp, co], "flagged_classification")
            cf.click(flag_cls, inputs=[ci, cm, cl, cp, co], outputs=None)

        # Translation Tab
        with gr.Tab("Translation"):
            with gr.Row():
                with gr.Column():
                    ti = gr.Textbox(lines=5, label="Source Text")
                    with gr.Row():
                        tm = gr.Dropdown(["OpenAI", "Ollama"], value="Ollama", label="Provider")
                        tl = gr.Dropdown(ollama_models, value="gemma3:4b", label="Local Model")
                    ts = gr.Textbox(label="From Language", value="English")
                    tt = gr.Textbox(label="To Language", value="Persian")
                    tn = gr.Radio(["Formal", "Informal"], value="Formal", label="Tone")
                    with gr.Row():
                        tb = gr.Button("Translate", variant="primary")
                        tf = gr.Button("🚩 Flag Result")
                to = gr.Textbox(lines=8, label="Translation Result")
            
            tb.click(handle_tra, inputs=[ti, tm, tl, ts, tt, tn], outputs=to)
            tra_callback.setup([ti, tm, tl, ts, tt, tn, to], "flagged_translation")
            tf.click(flag_tra, inputs=[ti, tm, tl, ts, tt, tn, to], outputs=None)

if __name__ == "__main__":
    logger.info("Application starting...")
    demo.launch()