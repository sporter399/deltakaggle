from flask import Flask, render_template
from arrayAPI import array_api



app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
)

app.register_blueprint(array_api)

@app.route("/")
def serve_vue_app():
    return (render_template('index.html'))

@app.route('/array', methods = ['GET'])
def server_array():
    return jsonify({'animals': array})

@app.after_request
def add_header(req):
    req.headers["Cache-Control"] = "no-cache"
    return req

if __name__ == "__main__":
    app.run(debug=True)
