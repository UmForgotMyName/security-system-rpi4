import os
from flask import Flask, render_template, send_from_directory, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    photos_with_time = get_photos_with_time()
    return render_template('index.html', photos_with_time=photos_with_time)

@app.route('/get_photos')
def get_photos():
    photos_with_time = get_photos_with_time()
    return jsonify({'photos': photos_with_time})

@app.route('/photos/<filename>')
def display_photo(filename):
    return send_from_directory('static/photos', filename)

def get_photos_with_time():
    photo_dir = 'static/photos'
    if os.path.exists(photo_dir):
        photos = [photo for photo in os.listdir(photo_dir) if photo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        photos_with_time = []

        for photo in photos:
            photo_path = os.path.join(photo_dir, photo)
            creation_time = os.path.getctime(photo_path)
            formatted_time = datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            photos_with_time.append({'filename': photo, 'created_at': formatted_time})

        return photos_with_time
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
