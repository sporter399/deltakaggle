from flask import Flask, render_template


app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
)

@app.route("/")
def serve_vue_app():
    return (render_template('index.html'))

@app.after_request
def add_header(req):
    req.headers["Cache-Control"] = "no-cache"
    return req

if __name__ == "__main__":
    app.run(debug=True)
