from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index(): #function
    return render_template('index.html')
@app.route("/welcome")
def welcome(): #function
    return render_template('welcome.html') #response 

if __name__ == "__main__": #This is will start the server
    app.run(debug=False) #Can be used to debug in the browser and auto reload when changes are made to the code