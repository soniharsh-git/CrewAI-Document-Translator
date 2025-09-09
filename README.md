# CrewAI Document Translator

## 📚 Project Overview
CrewAI Document Translator is a Python backend application that automates the translation of academic papers from their original language into a target language (configured in `config.yaml`).  
It preserves the document’s structure (tables, footnotes, formatting) while simulating the translation process.

---

## ⚡ Features
- Parses `.docx` academic documents into structured data.
- Simulates translation to target language (configured in `config.yaml`).
- Reconstructs and outputs the translated document as a `.docx` file.
- Maintains original formatting: bold, italics, alignment, and tables.

---

## ✅ How to Run the Project

### 1️⃣ Install dependencies:
```bash
pip install crewai python-docx pyyaml requests
