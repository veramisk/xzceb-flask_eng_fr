from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    french_text= translator.english_to_french(textToTranslate)
    return french_text
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
textToTranslate = request.args.get('textToTranslate')
english_text=translator.french_to_English('textToTranslate')
   return english_text
 return "Translated text to English"

@app.route("/")
def renderIndexPage():
   return render_template("index.html")

 if__name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



