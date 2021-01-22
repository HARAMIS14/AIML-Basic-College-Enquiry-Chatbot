from flask import Flask, render_template, request
import os
import aiml                                                          #import all modules

app = Flask(__name__)                                                #created instance of flask 

BRAIN_FILE="./pretrained_model/aiml_pretrained_model.brn"            #loaded brain file
k = aiml.Kernel()                                                    #created kernel object

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)                                          #if brain file exists in os path load the brain file
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)                                          # else learn files and save brain file

@app.route("/")                                                      #initialise app route
def home():
    return render_template("home.html")                              #get template file to display

@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')                                  #get user message in the form of query
    response = k.respond(query)                                      #stores response
    if response:
        return (str(response))               
    else:                                                            #response based on condition
        return (str("Information not found. Please check the website: https://phcet.ac.in/"))              
if __name__ == "__main__":                                           #app.run()
    app.run(host='127.0.0.7', port='5000')


