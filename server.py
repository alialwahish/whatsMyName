from flask import Flask,request,render_template,redirect
app=Flask(__name__)
@app.route('/')
def index():
    
    return render_template('index.html')
@app.route("/process",methods=["POST"])
def printit():
    print request.form["yrNam"]
    name=request.form["yrNam"]
    return render_template('index.html',name=name)
app.run(debug=True)