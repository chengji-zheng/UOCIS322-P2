"""
    CIS322 Project2 - Re-arrange Project 1 in Flask

        A practice of using render_template, send_from_directory


    localhost:8888/ <//>

"""

from flask import Flask, send_from_directory, render_template, request, abort

app = Flask(__name__)


# Handling 200
# Checking for specific html file that correspond to the name requested

@app.route("/<path:name>")
def ok(name):
    if ("//" in name) or (".." in name) or ('~' in name):
        abort(403)
    return send_from_directory("web/", name)

# Handling 404
@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

# Handling 403
@app.errorhandler(403)
def error_403(e):
        return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
  
