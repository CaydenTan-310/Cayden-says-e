from flask import Flask, request, render_template, redirect, g, session
from flask_session import Session
import json

app = Flask(__name__)
app.secret_key = "xT%P$b6*3$#V*$@^#8#%&L#SJz4PzN8UH(EBUPQUdH^#8*dw@@^7T6&u#68#6IYY2U*z3#36ff)H"

@app.route("/", methods=['POST'])
def hello():
  desc = request.form['question']
  answer = ""
  
  if "answers_string" in session:
    answer_dict = json.loads(session["answers_string"])

  counter = 0
  
  if "pythagoras" in desc:
    answer = "a² + b² = c²"
    counter = 1
  if "circle" in desc:
    answer = "Area: πr², Perimeter:2πr"
    counter = 1
  if "triangle" in desc:
    answer = "Area: ½bh"
    counter = 1

  if counter == 0:
    output = "Sorry I don't really understand. Please use different words?"
  else:
    output = answer + " Hope this was helpful :)"
  
  if(not (answer_dict["chats"][-1]["question"] == desc and answer_dict["chats"][-1]["answer"] == output) and desc !=  ""):
    answer_dict["chats"].append(
      {
        "question": desc,
        "answer": output
      }
    )
  session["answers_string"] = json.dumps(answer_dict)
  print(answer_dict)
  return render_template('index.html', allChats = answer_dict["chats"])

@app.route("/")
def helloBefore():
  answer_dict = {
    "chats": [
      { "question": "",
        "answer": "How can I help you today?"
      }
    ]
  }
  try:
    answer_dict = json.load(session["answers_string"])
  except:
    session["answers_string"] = json.dumps(answer_dict)
  
  
  return render_template('index.html', allChats = answer_dict["chats"])

if __name__ == "__main__":
  app.run(debug=True)



  