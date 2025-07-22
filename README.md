\# 📚 RAG\_bangla – Textbook-Based QA in Bangla \& English

Here is your complete, professional-grade README.md file for your RAG QA project. You can paste this directly into a new file named README.md in the root of your GitHub repo:



---





\# 📚 RAG\_bangla – Textbook-Based QA in Bangla \& English



A fully local Retrieval-Augmented Generation (RAG) system that answers questions in Bangla or English from a textbook PDF — using FAISS, sentence-transformers, and a local Ollama LLM (e.g. Mistral or Gemma). Comes with both a Streamlit web UI and a FastAPI-powered REST endpoint.



> 💬 Example: “অনুপমের ভাষায় আদর্শ মানুষ কে?”  

> ✅ Answered from actual content inside your PDF.



---



\## 🔍 Features



\- ✅ Upload \& chunk Bangla/English textbook PDFs

\- ✅ Generate embeddings with `sentence-transformers`

\- ✅ Store/retrieve chunks with `FAISS` (long-term memory)

\- ✅ Answer questions via local LLMs (Ollama: Mistral, Gemma)

\- ✅ Clean, friendly Streamlit web interface

\- ✅ REST API with FastAPI (POST /ask)

\- ✅ Multilingual: English + Bengali

\- ✅ Fully local, secure, and open-source



---



\## 📁 Project Structure



```



RAG\\\_bangla/

│

├── data/                 # Contains uploaded PDF \& chunked JSON

├── preprocessing/        # Script for text extraction \& chunking

│   └── chunk\\\_text.py

├── embeddings/           # Embedding generation and FAISS indexing

│   └── generate\\\_embeddings.py

├── model/                # RAG logic and Ollama integration

│   └── rag\\\_qa.py

├── ui/                   # Streamlit web UI

│   └── app.py

├── api/                  # FastAPI REST backend

│   └── main.py

└── requirements.txt



````



---



\## ⚙️ Setup Instructions



\### 1. Clone the Repo \& Set Up Environment



```bash

git clone https://github.com/ariyanshuddho/RAG\_bangla.git

cd RAG\_bangla

python -m venv venv

venv\\Scripts\\activate    # Windows

````



\### 2. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 3. Install Ollama and Pull Model



```bash

ollama run mistral     # Or: ollama run gemma

```



---



\## 🧩 Preprocess PDF



Put your textbook PDF in the `data/` folder. Then run:



```bash

python preprocessing/chunk\_text.py

```



This will save cleaned, chunked data as `data/chunks.json`.



---



\## 💡 Generate Embeddings



```bash

python embeddings/generate\_embeddings.py

```



This stores FAISS index (`data/faiss\_index.index`) and chunk IDs.



---



\## 🧠 Ask Questions (CLI)



```bash

python model/rag\_qa.py

```



---



\## 🌐 Web Interface (Streamlit)



```bash

streamlit run ui/app.py

```



---



\## 🔌 API Access (FastAPI)



```bash

uvicorn api.main:app --reload

```



Try it at:



\* Docs: \[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

\* POST: `/ask` with `{"question": "..."}`



---



\## 📦 Requirements



\* Python 3.10+

\* Ollama installed and model downloaded

\* Windows (tested), Linux/Mac compatible



---



\## ✅ Example Questions



| Language | Sample Question                              |

| -------- | -------------------------------------------- |

| Bangla   | অনুপমের ভাষায় আদর্শ মানুষ কে?               |

| English  | What is Anupam's definition of an ideal man? |



---



\## 🛠️ Technologies Used



\* Python, FAISS, sentence-transformers

\* Ollama (Mistral, Gemma)

\* Streamlit for UI

\* FastAPI for API

\* JSON \& PDF parsing with PyMuPDF



---



\## 🔐 Notes



\* No OpenAI API required — fully local

\* Handles both long-term (FAISS) and short-term memory

\* RAG structure can be swapped to use API-based LLMs too



---



\## 🙌 Author



\*\*Ariyan Shuddho\*\*

🔗 \[github.com/ariyanshuddho](https://github.com/ariyanshuddho)



---



\## 📄 License



MIT License – free to use, modify, and share.





