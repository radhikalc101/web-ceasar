from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius:10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <!-- create your form here-->
        <form method='POST'>
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label>
            <label>
                <textarea name="text">{encrypted}</textarea>
            </label>
            <input type="submit" value="Submit Quary"/>

    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot_int = int(request.form['rot'])
    text_str = request.form['text'] 
    encrypted_string = rotate_string(text_str, rot_int)
    #return <h1> + encrypted_string + </h1>
    return form.format(encrypted=encrypted_string) 

@app.route("/")
def index():
    return form.format(encrypted='')

app.run()