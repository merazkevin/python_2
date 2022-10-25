# localhost:5000/ - have it say "Hello World!"1
# localhost:5000/dojo - have it say "Dojo!"1
# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
# Create one url pattern and function that can handle the following examples
#  (HINT: int() will come in handy! For example int("35") returns 35):

# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times


from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'
    
@app.route('/dojo/')
def dojo():
    return 'dojo'

@app.route('/say/flask')
def flask():
    return 'Hi flask!'

@app.route('/say/<name>')
def hi_John(name):
    return f'Hi {name}!'

@app.route('/repeat/<word>/<int:number>')
def repeat(word, number):
    return word * number

    # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)