
---

# Text to Emoji Generator

This project is a simple web application that converts user-provided text into emoji-based responses. It uses the **Gemini AI** API for text generation and is built with the **Flask** framework.

## Features
- Converts any given text to an emoji-based response using AI.
- Built with Flask, providing a lightweight server.
- Supports WebSockets for real-time communication.
- Uses the Gemini API for generating emoji-based content.

## Requirements

Before you run the project, you need to install the required Python libraries. The dependencies are listed in `requirements.txt`.

### Install dependencies:
1. Clone the repository to your local machine:
    ```bash
    git clone <repo-url>
    cd <repo-name>
    ```

2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **Linux/Mac**:
        ```bash
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Create `.env` File:
Before running the application, you need to set up the **Gemini API key**. To do so:

1. Create a `.env` file in the root directory of the project.
2. Inside the `.env` file, add the following line (replace `<YOUR_API_KEY>` with your actual Gemini API key):
    ```bash
    GOOGLE_API_KEY=<YOUR_API_KEY>
    ```

   This allows the application to securely access your Gemini API key without exposing it in the code.

## Running the Application

1. Start the Flask development server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to see the application in action.

## Usage

1. On the homepage, enter your desired text in the input field.
2. Click the "Generate Emoji" button to see the emoji-based response.
3. You can also interact with the system in real-time via WebSockets.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **SocketIO**: For real-time communication between the client and server.
- **Gemini AI**: For generating text-to-emoji responses.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

    