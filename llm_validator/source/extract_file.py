import pdfplumber
import gradio as gr
import os

def extract_text(doc):
    text = ""
    ext = os.path.splitext(doc.name)[1].lower()
    try:
        if ext == ".pdf":
            with pdfplumber.open(doc.name) as f :
                for pdf in f.pages:
                    text += pdf.extract_text() + "\n"
        else:
            return gr.update(value="❌ Unsupported file type. Upload PDF or DOCX.", visible=True)

    except Exception as e:
        return e

    return gr.update(value=f"✅ Extracted Text for Trade ID :\n\n {text}...", visible=True)




