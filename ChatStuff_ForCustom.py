## GPT3 file
import os
import openai

import LogsFileHandler as L
import txtHandler as T

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

def ask(question, prompt_, eng, 
        temp, top_p_val, token_lim, stopper, 
        freq_pen, pres_pen, retries):
    prompt_ = prompt_ + "\nYou: " + question + "\nBot: "
    response = completion.create(
        prompt = prompt_, 
        engine = eng,
        temperature = float(temp),
        max_tokens = int(token_lim),
        top_p = float(top_p_val),
        stop = [stopper],
        frequency_penalty = float(freq_pen) ,
        presence_penalty = float(pres_pen),
        best_of = int(retries)
        )

    answer = response.choices[0].text.strip()
    print(response)
    print(L.loggings().Text_writer2(answer, ques =  prompt_))
    return response.choices[0].text.strip()
