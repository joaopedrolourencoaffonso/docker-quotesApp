from flask import Flask, render_template, redirect, jsonify, send_file
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html");
    
# Example of a client-side route
@app.route('/quotes', methods=['GET'])
def get_quotes():
    # Make a request to the external API
    external_api_url = "http://quotes-api:8080/quotes"
    response = requests.get(external_api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response to the client
        return jsonify(response.json())
    else:
        # If there was an error, return an error message or handle it accordingly
        return jsonify({"error": "Failed to fetch quotes"}), 500
    
@app.route('/imagemDeFundo', methods=['GET'])
def imagemDeFundo():
    # Replace 'https://example.com/api/get_image' with the actual image API endpoint
    image_api_url = 'http://images-api:8080/imagemDeFundo'

    try:
        # Make a request to the image API
        response = requests.get(image_api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the content type from the response headers
            content_type = response.headers.get('Content-Type', '')

            # Check if the response is an image (you might want to refine this check based on your API)
            try:
                # Return the image as a response
                return response.content
            except:
                # Return an error message if the response is not an image
                return jsonify({"error": "The response is not an image"}), 500
        else:
            # Return an error message if the request to the image API failed
            return jsonify({"error": "Failed to fetch image"}), 500

    except Exception as e:
        # Handle other exceptions (e.g., network errors)
        return jsonify({"error": str(e)}), 500

app.run(host='0.0.0.0', port=8080,debug=True);
