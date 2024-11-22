from flask import Flask, render_template, request, send_file
import qrcode
from PIL import Image
import os
import requests
from favicon import get as get_favicon

app = Flask(__name__)

# Path to store QR Code images
QR_CODE_PATH = "static/qr_codes"
if not os.path.exists(QR_CODE_PATH):
    os.makedirs(QR_CODE_PATH)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_qr_code():
    input_text = request.form.get('input_text')  # Retrieve the user input from the form
    if not input_text or not input_text.strip():
        return "Input text cannot be empty!", 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text.strip())
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Try fetching the favicon
    try:
        icons = get_favicon(input_text.strip())
        if icons:
            icon = icons[0]
            response = requests.get(icon.url, stream=True)
            if response.status_code == 200:
                favicon_image = Image.open(response.raw).convert("RGBA")
                favicon_image = favicon_image.resize((120, 120))

                # Center the favicon on the QR code
                qr_width, qr_height = qr_image.size
                icon_width, icon_height = favicon_image.size
                position = ((qr_width - icon_width) // 2, (qr_height - icon_height) // 2)
                qr_image.paste(favicon_image, position, mask=favicon_image)
    except Exception as e:
        print(f"Error fetching favicon: {e}")  # Log errors but continue without favicon

    qr_image_path = os.path.join(QR_CODE_PATH, "qr_code.png")
    qr_image.save(qr_image_path)

    return render_template('result.html', qr_code_path=qr_image_path, input_text=input_text)


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files or not request.files['image']:
        return "No file uploaded!", 400

    uploaded_file = request.files['image']
    if uploaded_file.filename == '':
        return "No file selected!", 400

    image_path = os.path.join(QR_CODE_PATH, "uploaded_image.png")
    uploaded_file.save(image_path)

    # Load QR code and uploaded image
    qr_code_path = os.path.join(QR_CODE_PATH, "qr_code.png")
    qr_image = Image.open(qr_code_path)
    overlay_image = Image.open(image_path).convert("RGBA")
    overlay_image = overlay_image.resize((120, 120))  # Resize the uploaded image to fit the QR code

    # Center the uploaded image on the QR code
    qr_width, qr_height = qr_image.size
    overlay_width, overlay_height = overlay_image.size
    position = ((qr_width - overlay_width) // 2, (qr_height - overlay_height) // 2)
    qr_image.paste(overlay_image, position, mask=overlay_image)

    qr_with_image_path = os.path.join(QR_CODE_PATH, "qr_with_image.png")
    qr_image.save(qr_with_image_path)

    return render_template('result.html', qr_code_path=qr_with_image_path)


@app.route('/download_qr_code', methods=['GET'])
def download_qr_code():
    qr_code_path = os.path.join(QR_CODE_PATH, "qr_with_image.png")
    if not os.path.exists(qr_code_path):
        qr_code_path = os.path.join(QR_CODE_PATH, "qr_code.png")
    return send_file(qr_code_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
