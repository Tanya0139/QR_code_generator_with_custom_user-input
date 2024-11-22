<img width="843" alt="Screenshot 2024-11-22 at 3 44 12 PM" src="https://github.com/user-attachments/assets/78bf00c5-32ff-47ab-8b28-72a54b554e55"># QR Code Generator with Custom Input and User Interaction

This project is a simple web-based QR Code Generator built using Python (Flask framework) and HTML/CSS for the frontend. It allows users to generate QR codes by entering a URL and provides additional functionality to overlay custom images on the QR code.

## Features

- **Dynamic QR Code Generation**: Enter a URL to generate a QR code instantly.
- **Custom Image Overlay**: Automatically fetches the favicon of the entered URL or allows the user to upload an image if the favicon is unavailable.
- **Download Option**: Users can download the generated QR code with or without a custom image.
- **Simple and User-Friendly Interface**: Designed with a clean and modern UI.
- 
## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Dependencies**:
  - `qrcode`
  - `Pillow`
  - `requests`
  - `flask`
  - `favicon`

## Project Structure

```
project/
├── templates/
│   ├── index.html       # Homepage with input form
│   ├── result.html      # Displays the generated QR code
├── static/
│   ├── styles.css       # Optional custom styles
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to use the app.

## Usage

1. On the homepage, enter a valid URL and click "Generate QR Code".
2. If a favicon is available for the URL, it will be overlaid on the QR code.
3. If no favicon is available, you can upload an image to overlay.
4. View the generated QR code and use the buttons to:
   - **Download** the QR code.
   - **Upload a custom image** to replace the favicon.

## Deployment

You can deploy this project on any platform supporting Python and Flask, such as:

- **Heroku**
- **PythonAnywhere**
- **Railway.app**

Follow the hosting platform’s instructions for deploying Flask applications.

## Screenshots
<img width="841" alt="Screenshot 2024-11-22 at 3 44 37 PM" src="https://github.com/user-attachments/assets/18cf91b0-afb2-4db3-a378-3f1eeb4d1408">

- **Homepage**:
  - Enter the URL in the input box to generate a QR code.

- **Result Page**:
  - Displays the generated QR code.
  - Includes options to download the QR code or upload a custom image.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Developed with ❤️ by Tanya.
- Special thanks to the maintainers of the `qrcode` and `flask` libraries.

---

Feel free to reach out for feedback, suggestions, or collaboration opportunities!
