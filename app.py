from flask import Flask, render_template, request, jsonify
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import time

app = Flask(__name__, static_folder='static')
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
llm_groq = ChatGroq(
    api_key=groq_api_key,
    model_name='llama3-8b-8192',
    temperature=0.5
)

template = """
As an Islamic scholar, provide accurate and concise answers to questions about Islam. 
Follow this format:
1. Begin with "Bismillah" and give a clear, brief answer.
2. Include relevant Quranic verses or Hadith with proper references.
3. If the question relates to fiqh, mention the school of thought if applicable.
Structure your response:
- Answer: [Your response]
- Reference: [Quran Surah:Verse] or [Hadith Book:Number]
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()

chain = (
        {"question": RunnablePassthrough()}
        | prompt
        | llm_groq
        | output_parser
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('input_text')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    try:
        start_time = time.time()
        answer = chain.invoke(user_input)
        processing_time = round(time.time() - start_time, 2)
        formatted_answer = answer.replace('\n', '<br>')

        return jsonify({
            'answer': formatted_answer,
            'processing_time': processing_time
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)