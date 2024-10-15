from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if not username or not password or not email:
        flash('All fields are required!')
        return redirect(url_for('index'))

    if '@' not in email:
        flash('Invalid email address!')
        return redirect(url_for('index'))

    flash('Registration successful!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
