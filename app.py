from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Yeh aapke templates folder se index.html ko load karega
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
