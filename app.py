from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = 'API-KEY'  # Replace with your actual ChatGPT API key

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']

        try:
            response = openai.Completion.create(
                engine='text-davinci-003',  
                prompt=f'User: {prompt}\nAssistant:',
                max_tokens=50
            )

            assistant_response = response.choices[0].text.strip()
            return render_template('results.html', prompt=prompt, assistant_response=assistant_response)
        except openai.error.OpenAIError as e:
            error_message = f"API request error: {str(e)}"
            return render_template('error.html', error_message=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
