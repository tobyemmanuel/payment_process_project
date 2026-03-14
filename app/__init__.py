from flask import Flask, render_template, request, redirect, url_for, flash


def create_app():
    app = Flask(__name__)
    app.secret_key = "jfdjdhdfdhdfk"

    @app.route("/")
    def home():
        
        user = {
            "name": "Emmanuel Senior Dev",
            "gender": "male",
            "age": 90
        }
        
        return render_template("home.html", user = user)
        # return "<h1>Hello! we setup flask before we were away.</h1> <p>Hello, World!</p>"

    @app.route("/login")
    def login():
        return render_template("login.html")
    
    
    @app.route("/process_login", methods=["POST"])
    def process_login():
        
        database = (
            {"username": "emmanuel", "password": "12345678"},
            {"username": "semilore", "password": "12345678"},
        )
        
        error = ""

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
        
            for user in database:
                if user["username"] == username and user["password"] == password:
                    return redirect(url_for("dashboard"))
                else:
                    error = "Invalid credentials"   
                    flash(error)    
        
        return redirect(url_for("login"))
        # return render_template("login.html", error = error, username = username)
    
    
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")
    
    
    return app


