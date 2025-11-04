##import Flask class from flask package
from Flask import Flask

##Start flask nirmal insatnce 
app = Flask(__name__)
##  It is for defining endpoint
@app.route("/")### mail root url

##defined function fo home means main url call or endpoint
def home():
    return "Application deployment successfully done for Production env//new Features added on 4th November"


@app.route("/nirmal")

def nirmal():

    return "This is nirmal call"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
