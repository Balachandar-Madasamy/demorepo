from source.extract_file import *
from llm_call import calling
from config.prompt import prompt
from llm_validator.export2table import extract2table

def app_interface(file,id):
    if file is None:
        return gr.update(value = "File is Empty , Please provide a valid file ",visible=True)
    # gr.update(value = f"File is successfully uploaded {file} | {id}",visible=True)
    docs = extract_text(file)
    inp = prompt + str(docs)
    print(f"Successfully parsed the Docs prompt ::: ",inp)
    out = calling(inp)
    df = extract2table(out)
    return gr.update(value = f"File successfully parsed : \n Here is the LLM Output \n \n {df}",visible=True)


with gr.Blocks() as demo:
    gr.Image(value="img.png")
    gr.Markdown("### 📑 Term Sheet Validator")
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label='Upload a Term sheet File',
                file_types = ['.pdf','.docx'],
            )
        trade_id_input = gr.Textbox(
                label="Enter Trade ID",
                placeholder="e.g., T12345"
            )
    output_text = gr.Textbox(label="Output",visible=False)
    # output = gr.Textbox(label="Processed Output Results ")

    submit_button = gr.Button("Process the Term sheet")
    submit_button.click(fn = app_interface,inputs=[file_input,trade_id_input],outputs =[output_text],api_name='llm_validator')


demo.launch()