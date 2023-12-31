from flask import Flask, jsonify, send_from_directory
from extensions import mongo, limiter, cors
from handler import user, upload, video
import config

app = Flask(__name__, static_folder="./dist")
app.config.from_object(config)

mongo.init_app(app)
limiter.init_app(app)
cors.init_app(app)

app.register_blueprint(user.bp)
app.register_blueprint(upload.bp)
app.register_blueprint(video.bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if "." in path:
        return send_from_directory(app.static_folder, path)
    
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify(error="ratelimit exceeded", message=str(e.description)), 429

if __name__ == '__main__':
    app.run()
