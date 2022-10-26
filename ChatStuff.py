## GPT3 file
import os
import openai

from dotenv import load_dotenv
load_dotenv()

import LogsFileHandler as L
import txtHandler as T

openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
Bot: I am OpenAI's GPT3. How can I help you today?
'''

# The consumption rate of credit was enormous with this trial thing. Better to keep it commented unless someone is very much curious about how this works
# def ask2(question):
#     halfans = ask(ques = question, prompt_ = 2, text = True)
#     ans = ask(ques = halfans, prompt_ = 1, text = True)
#     return ans

def ask(ques, prompt_ , text = None ):
    if prompt_ == 1:
            if text:
                prompt_ = T.GenZ2()
            else: 
                prompt_ = T.GenZ() 
            d = T.GenZSettings()
            eng = "text-davinci-002"
            temp = d["temp"]
            top_p_val = d["top_p_val"]
            freq_pen = d["freq_pen"]
            pres_pen = d["pres_pen"]
    elif prompt_ == 2:
            if text:
                prompt_ = T.ToneChanger2()
            else: 
                prompt_ = T.ToneChanger()
            eng = "text-curie-001"
            d = T.CasSettings()
            temp = d["temp"]
            top_p_val = d["top_p_val"]
            freq_pen = d["freq_pen"]
            pres_pen = d["pres_pen"] 
    elif prompt_ == 0:
        prompt_ = start_chat_log
        eng = "text-davinci-002" 
    
    prompt_ = prompt_ + " " + ques + "\nCooler Version: "
    
    response = completion.create(
        prompt=prompt_, 
        engine=eng,
        temperature= temp,       ##  0.3
        max_tokens= 150,   
        top_p= top_p_val,           ## 1
        stop = ['stop'],  
        frequency_penalty= freq_pen,  ## 1
        presence_penalty= pres_pen,  ## 0.3
        best_of = 3
        )
    answer = response.choices[0].text.strip()
    print(L.loggings().Text_writer(ques, answer))
    return response.choices[0].text.strip()
