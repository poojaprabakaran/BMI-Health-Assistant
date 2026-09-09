# 🤖 Health Assistant for Fitness

An AI-powered health and fitness assistant built using Python, Streamlit, and Google Gemini API. The application calculates the user's BMI from their height and weight and uses the BMI value as additional context while answering general fitness, diet, and lifestyle-related questions.

## 📌 About the Project

The Health Assistant for Fitness provides an interactive interface where users can enter their height and weight to calculate their BMI and then ask questions related to fitness and healthy lifestyle choices.

The application uses Google Gemini Generative AI to generate responses based on the user's question and BMI value where relevant.

✨ Features

* 📏 Calculate BMI using height and weight
* 🧮 Display the calculated BMI value
* 🤖 Generate AI-powered responses using Google Gemini
* 🏃 Provide general fitness and lifestyle suggestions
* 🥗 Answer general diet-related questions
* 🔍 Use BMI as context when generating relevant responses
* ⚠️ Provide a disclaimer for medication-related questions
* 🚫 Avoid diagnosing medical conditions
* 🎨 Simple and interactive Streamlit interface

🛠️ Technologies Used

Python – Application development

Streamlit – Interactive web application

Google Gemini API – Generative AI responses

python-dotenv – Environment variable management

Pandas – Data handling

🔄 How It Works

The application follows a simple workflow:

User enters Height & Weight
            ↓
       BMI Calculation
            ↓
       BMI displayed
            ↓
User enters a health/fitness question
            ↓
    BMI + Question sent to
       Google Gemini API
            ↓
       AI-generated response

The BMI is calculated using the formula:

BMI = Weight (kg) / Height² (m²)

The calculated BMI is included in the prompt when the user's question is relevant to their BMI.

🤖 Generative AI Implementation

The application integrates Google Gemini Generative AI to provide contextual responses to users' health and fitness questions.

The user's BMI and question are dynamically incorporated into a prompt before being sent to the Gemini model. The prompt instructs the model to:

Consider the user's BMI when relevant

Provide general fitness, diet, and lifestyle recommendations

Avoid diagnosing medical conditions

Recommend consulting a physician for medication-related questions

This demonstrates the use of prompt engineering and contextual Generative AI within a Streamlit application.

💡 Example Questions

Users can ask questions such as:

What exercises are suitable for me?

How can I improve my fitness?

What type of diet should I follow?

How can I maintain a healthy lifestyle?

What exercises can help with weight management?

🔐 API Configuration

The application uses a Gemini API key stored as an environment variable.

Create a .env file:

GEMINI_API_KEY=your_api_key_here

The API key is loaded using python-dotenv.

Important: Never upload your .env file or API key to GitHub. Add .env to your .gitignore file.

▶️ Running the Project

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run bmi.py

⚠️ Disclaimer

This application is intended for general health, fitness, diet, and lifestyle information only.

It is not intended to provide medical diagnosis, treatment, or professional medical advice. Medication-related questions should be discussed with a qualified healthcare professional.

🔮 Future Enhancements

* 📊 Add BMI category classification
* 📈 Add BMI tracking and history
* 🏋️ Provide personalized workout recommendations
* 🥗 Generate personalized meal suggestions
* 💬 Add conversational chat history
* 👤 Add user profiles
* 📱 Improve mobile responsiveness

👩‍💻 Author

Pooja Prabakaran

Built as a practical Generative AI and Streamlit project to explore the integration of Google's Gemini API with a Python-based interactive application.
