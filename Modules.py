import enum
from flask import Flask, redirect, url_for, render_template , request
import datetime
import pytz

import ChatStuff as C
import ChatStuff_ForCustom as F
import txtHandler as T
from Modules import *

Creds = {
    "user"  :   "user",
    "pass"  :   "user"
}

def DatetimeReturn():
    return datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

class Tones(enum.Enum):
    gen = 1
    cas = 2
    gen2 = 3

def ToneChecker(r):
    if r == "gen":     return 1
    elif r == "cas":   return 2
    elif r == "gen2":   return 3

def editer():
    prompt = request.form.get("prompt")
    settings = request.form.get("settings")
    Fil = request.form.get("type")
    T.fileSaver(prompt, settings, Fil)
    return render_template("AdminEditor.html", content = {"content": "FILES HAVE BEEN UPDATED"})

def logginchecker():
    user = request.form.get("username")
    passw = request.form.get("password")
    if (request.form["rad"] != None):
        rad = request.form["rad"]
        if rad == "gen":
            prompt = T.GenZ()
            settings = T.GenZSettings()
        else: 
            prompt = T.ToneChanger()
            settings = T.CasSettings()
    if user == Creds["user"] and passw == Creds["pass"]:
        return render_template("AdminEditor.html", content = {"prompt":prompt, "settings":settings, "Fil" : rad})
    else: return render_template("adminLogin.html", content = "LOGIN NOT SUCCESSFUL. Either username or password was incorrect.")

def user():
    if (request.form["rad"] != None):
        rad = request.form["rad"]
    tone = Tones.rad
    question = request.form["question"]
    if tone == 3:
      answer = C.ask2(question)
    else:
        answer = C.ask(question,tone) 
    # if (custom):
    #     return render_template("CustomEntries.html")
    # else: 
    # return redirect(url_for("answer", ans = answer))
    return render_template("index.html", content = answer)

def custom():
    render_template("CustomEntries.html")
    
    eng= request.form.get("engine")
    temp= request.form.get("temp")
    top_p_val= request.form.get("top_p")
    token_lim= request.form.get("tokens")
    stopper = request.form.get("stop")
    freq_pen= request.form.get("freq_pen")
    pres_pen= request.form.get("pres_pen")
    retries= request.form.get("best_of")
    prompt_ = request.form.get("prompt")
    question = request.form.get("question")
    
    answer = F.ask(question, prompt_, eng, 
        temp, top_p_val, token_lim, stopper, 
        freq_pen, pres_pen, retries)
    return render_template("CustomEntries.html", content = answer)
