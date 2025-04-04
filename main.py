from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Initialize counter
counter = 0

@app.route('/')
def index():
    global counter
    # Check if counter reached 100
    if counter == 100:
        return render_template('index.html', counter=counter, message="Counter reached 100. Please restart.")
    
    return render_template('index.html', counter=counter, message="")

@app.route('/count_up')
def count_up():
    global counter
    if counter < 100:
        counter += 1
    return redirect(url_for('index'))

@app.route('/count_down')
def count_down():
    global counter
    if counter > 0:
        counter -= 1
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global counter
    counter = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
