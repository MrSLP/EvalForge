from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/students")
    def students():
        return render_template("students.html")

    @app.route("/timeline")
    def timeline():
        return render_template("timeline.html")

    @app.route("/vault")
    def vault():
        return render_template("vault.html")

    @app.route("/analytics")
    def analytics():
        return render_template("dashboard.html")  # If "analytics" is in "dashboard.html"

    @app.route("/eligibility_viewer")
    def eligibility_viewer():
        return render_template("eligibility_viewer.html")

    @app.route("/eligibility_comparison")
    def eligibility_comparison():
        return render_template("eligibility_comparison.html")

    return app