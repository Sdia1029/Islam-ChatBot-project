

# 🕌 Islamic ChatBot

A real-time Islamic ChatBot powered by the **LLaMA 3 8B** model and **Groq API**, designed to provide authentic responses grounded in Islamic teachings. The chatbot begins each interaction with **"Bismillah"** and cites relevant **Quranic verses** or **Hadiths** to ensure accuracy and reliability.

---

## ✨ Features

- **Prompt Engineering**: Ensures responses emulate an Islamic scholar's tone and style.
- **Quran & Hadith References**: Provides citations from authentic Islamic sources.
- **Fast & Cost-Effective**: Utilizes Groq API for rapid responses with minimal latency.
- **Lightweight Model**: Employs LLaMA 3 8B for efficient performance without compromising accuracy.
- **Modular Architecture**: Built with Flask and LangChain for seamless integration and scalability.

---

## 🧱 Tech Stack

- **Backend**: Flask
- **Frontend**: HTML/CSS (with optional enhancements using Bootstrap or Tailwind CSS)
- **AI Model**: LLaMA 3 8B via Groq API
- **Prompt Management**: LangChain
- **Deployment**: Localhost (with options for cloud deployment)

---

## 📁 Project Structure

```
Islam-ChatBot-Project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── background.jpg
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Groq API Key

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sdia1029/Islam-ChatBot-Project.git
   cd Islam-ChatBot-Project
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your Groq API key:

   ```bash
   GROQ_API_KEY=your_api_key_here
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

6. **Access the ChatBot**

   Open your browser and navigate to `http://127.0.0.1:5000` to interact with the chatbot.

---

## 🧠 Prompt Engineering Strategy

The chatbot is designed to:

- Begin each response with **"Bismillah"**.
- Provide answers that reflect the knowledge and demeanor of an Islamic scholar.
- Cite relevant **Quranic verses** or **Hadiths** to support its responses.
- Avoid conjecture by stating "Allah knows best" when uncertain.

---

## 🛡️ Ethical Considerations

- **Authenticity**: Responses are grounded in verified Islamic sources.
- **Transparency**: The chatbot acknowledges its limitations and refrains from providing speculative answers.
- **Respect**: Maintains a respectful and informative tone in all interactions.

---

## 📚 References

- [LangChain Documentation](https://docs.langchain.com/)
- [Groq API Documentation](https://docs.groq.com/)
- [LLaMA 3 Model Details](https://ai.meta.com/llama/)

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

## 🙋‍♀️ About the Author

**Sadia Eman Abdul Ghafoor**  
BS Data Science Student at Superior University 
Passionate about integrating AI with Islamic knowledge to create accessible educational tools.

---
