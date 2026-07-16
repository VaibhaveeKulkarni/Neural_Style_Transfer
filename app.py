from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

# HTML template for the main page
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Stylized Image</title>
  <style>
    body { font-family: sans-serif; text-align: center; margin-top: 50px; }
    img { max-width: 90%; height: auto; border: 2px solid #ccc; }
  </style>
</head>
<body>
  <h1>Your Stylized Image</h1>
  <img src="/output/output.png" alt="Stylized Image">
  <p>Image generated using Neural Style Transfer.</p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/output/<path:filename>')
def serve_output_image(filename):
    # Ensure the path is correct for where output_images is created
    return send_from_directory(os.path.join(os.getcwd(), 'output_images'), filename)

if __name__ == '__main__':
    # In a Colab environment, use a public URL if available, otherwise a simple run
    # For deployment, consider using a proper WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000, debug=True)
