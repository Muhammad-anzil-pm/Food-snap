from flask import Flask,render_template,request
from model_logic import yolo_model,prediction

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods = ['GET','POST'])
def create_user():
    if request.method == "POST":
        return render_template('foodsnap.html')
    else:
        return render_template('login.html')

@app.route('/analyze_image', methods = ['POST'])
def analyze_image():
    file = request.files['file']
    results = prediction(file)
    

def result_dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)