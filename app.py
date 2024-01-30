from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='/app')

# Sample user credentials (replace with a secure authentication mechanism in a real application)
valid_username = "user"
valid_password = "password"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == valid_username and password == valid_password:
        # In a real application, you'd typically use a secure session mechanism instead of a simple redirect
        return redirect(url_for('index'))
    else:
        return render_template('index.html', error='Invalid username or password')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
