

# Project Documentation: Flask ChatGPT Integration

This project is a simple web application that integrates with the ChatGPT API to provide a conversational assistant. Users can enter prompts or questions, and the assistant will generate responses using the ChatGPT model.

## Table of Contents
1. [Project Setup](#project-setup)
2. [API Integration](#api-integration)
3. [Web Application](#web-application)


## Project Setup<a name="Flask-chatgpt"></a>

To set up the project, follow these steps:

1. Clone the project repository from GitHub:
   ```
   git clone https://github.com/harish343/flask_chatgpt.git
   ```

2. Install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key for the ChatGPT API from OpenAI. Replace the placeholder `'YOUR_API_KEY'` with your actual API key in the code.

4. Set up a virtual environment (optional but recommended) and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

## API Integration<a name="api-integration"></a>

The project uses the OpenAI Python library to make API calls to the ChatGPT API. The API integration is implemented in the `app.py` file. Here's an overview of the API integration steps:

1. Import the `openai` module and set the API key:
   ```python
   import openai

   openai.api_key = 'YOUR_API_KEY'
   ```

2. Make API calls to the ChatGPT API:
   - Create a completion using the `openai.Completion.create()` method.
   - Set the appropriate parameters such as the engine, prompt, and max tokens.
   - Handle any API errors or exceptions using `try`-`except` blocks.

3. Parse the API response to extract the assistant's response.

## Web Application<a name="web-application"></a>

The Flask web application is implemented in the `app.py` file. It provides a simple user interface for interacting with the ChatGPT assistant. Here's an overview of the web application features:

1. Homepage:
   - Displays a form where users can enter prompts or questions.
   - Submits the form data to the server using a POST request.

2. Results page:
   - Displays the user's prompt and the assistant's response.
   - Renders the `results.html` template with the appropriate variables.

3. Error page:
   - Displays an error message if there is a problem with the API request.
   - Renders the `error.html` template with the appropriate error message.


## Testing<a name="testing"></a>

To run the application and test its functionality, follow these steps:

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Access the application in a web browser at `http://localhost:5000`.

3. Enter a prompt or question in the homepage form and submit it.

4. Verify that the results page displays the user's prompt and the assistant's response.

5. Test the error handling by intentionally causing an API request error.

   - Modify the code in `app.py` to trigger an error condition (e.g., remove the API key).
   - Submit a prompt in the homepage form and observe the error page.



## Conclusion

This documentation provides an overview of the Flask web application that integrates with the ChatGPT API. It covers the project setup, API integration, web application features, and testing instructions. 
