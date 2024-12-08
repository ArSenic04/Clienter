# React + Flask RAG Chatbot

This project is a **React Frontend** and **Flask Backend** chatbot application that utilizes Retrieval-Augmented Generation (RAG). The chatbot uses LangChain for document retrieval and Hugging Face transformers for text generation. It is designed to be deployed on **Vercel** using serverless functions for the backend.

---

## **Features**

- Frontend: **React** (TypeScript) for user interaction.
- Backend: **Flask** for handling chatbot API requests.
- RAG-based architecture:
  - **Document retrieval** using FAISS.
  - **Text generation** using Hugging Face `flan-t5-base`.
- Fully deployable to **Vercel**.

---
Prerequisites Frontend: Node.js \>= 16.0.0 npm or yarn Backend: Python
\>= 3.9 pip Setup and Development 1. Clone the Repository bash Copy code
git clone \<repository-url\> cd \<repository-name\> 2. Install
Dependencies For the Backend bash Copy code cd api pip install -r
requirements.txt For the Frontend bash Copy code cd frontend npm install
3. Run Locally Run Flask Backend bash Copy code cd api python chat.py
The backend will be available at http://localhost:5000.

Run React Frontend bash Copy code cd frontend npm start The frontend
will be available at http://localhost:3000.

Deployment on Vercel 1. Add vercel.json Ensure the vercel.json file is
present in the root directory:

json Copy code { \"version\": 2, \"builds\": \[ { \"src\":
\"api/chat.py\", \"use\": \"@vercel/python\" }, { \"src\":
\"frontend/package.json\", \"use\": \"@vercel/static-build\" } \],
\"routes\": \[ { \"src\": \"/api/(.\*)\", \"dest\": \"/api/chat.py\" },
{ \"src\": \"/(.\*)\", \"dest\": \"/frontend/\$1\" } \] } 2. Push Code
to GitHub Ensure your repository is hosted on GitHub, GitLab, or another
VCS.

3\. Deploy to Vercel Connect your repository to Vercel. Define the Build
Commands: Frontend: npm run build (Output: frontend/build). Backend:
Automatically detected in api/. 4. Add Environment Variables If your
chatbot relies on sensitive information or external storage, add these
under Vercel Settings \> Environment Variables.

5\. Test the Application Once deployed, test the application using the
Vercel-provided URL.

Frontend API Integration In the frontend React application, ensure API
calls use a relative path to the backend:

tsx Copy code const response = await axios.post(\'/api/chat\', {
message: userInput }); This ensures compatibility with Vercel\'s
serverless functions.

Key Dependencies Frontend React: \^18.0.0 Axios: \^1.0.0 Backend Flask:
\^2.3.3 Flask-CORS: \^3.0.10 Transformers: \^4.35.0 LangChain Community:
\^0.0.27 LangChain HuggingFace: \^0.3.15 FAISS: \^1.7.4 Example API
Request Request: json Copy code POST /api/chat Content-Type:
application/json

{ \"message\": \"What is the sales data for Q3?\" } Response: json Copy
code { \"response\": \"The sales data for Q3 shows an increase of 15%
compared to Q2.\" } Future Enhancements Add authentication for secure
API access. Integrate a cloud storage service for large datasets.
Improve response generation with advanced LLM models. Contributors Your
Name - Developer Open for collaboration. Feel free to raise issues or
contribute to the repository. License This project is licensed under the
MIT License. See the LICENSE file for details.

