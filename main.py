from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/drm')
def drm_player():
    video = request.args.get('video')
    token = request.args.get('token')
    if not video or not token:
        return "Missing video or token parameter."
    m3u8_url = f"https://media-cdn.classplusapp.com/drm/{video}/playlist.m3u8"
    return render_template('index.html', m3u8=m3u8_url, token=token)

@app.route('/')
def home():
    return "DRM Player is live. Use /drm?video=xxxx&token=yyyy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)