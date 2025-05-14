
```markdown
# 🛂 AI-Powered Document & KYC Verification API

A FastAPI-based backend system that leverages **OCR** and **LLM (Mistral AI)** to verify documents like Aadhaar, PAN, Driving License, Flight Tickets, and Train Tickets. Built with clean architecture, SOLID principles, and environment-based configurations using `.env`.

---

## 🧠 Tech Stack

- **Framework**: FastAPI
- **OCR**: EasyOCR / Tesseract + OpenCV
- **LLM Integration**: Mistral AI (via local Ollama or remote API)
- **Language**: Python 3.11+
- **Architecture**: Modular Clean Architecture
- **Dependency Management**: `pip` with `requirements.txt`
- **Environment Config**: Python-dotenv

---


## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/documentver.git
cd documentver
````

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root with the following variables:

```
MISTRAL_API_KEY=your_mistral_api_key_or_blank_for_local
MISTRAL_ENDPOINT=http://localhost:11434/api/generate  # or remote API endpoint
```

> ⚠️ Your `.env` file is ignored by Git using `.gitignore`.

### 5. Run the App

```bash
uvicorn app.main:app --reload
```

Visit your local server at: `http://127.0.0.1:8000/docs`

---

## 🖼️ How It Works

1. User uploads Aadhaar, PAN, License, or Ticket image.
2. OCR engine extracts raw text.
3. Mistral AI processes raw text and returns structured JSON (e.g., name, dob, doc number).
4. API responds with clean, verified information.

---

## 🧪 Example Output

**Input**: Aadhaar card image
**Output**:

```json
{
  "name": "Ganesh Jalindar Divekar",
  "dob": "31/03/1992",
  "aadhaar_number": "5296 6023 5315"
}
```

---

## 🔒 Security Notes

* `.env` is excluded via `.gitignore` to prevent leaking secrets.
* Always rotate API keys if shared by mistake.
* Use encrypted secret managers in production (AWS Secrets Manager, Vault).

---

## 👥 Contributing

1. Fork this repository
2. Create a new branch
3. Make changes and commit
4. Push your branch and create a PR

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔗 Useful Links

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Mistral AI](https://mistral.ai/)
* [EasyOCR GitHub](https://github.com/JaidedAI/EasyOCR)

---

## 💻 Author

Built with ❤️ by **Ganesh Divekar**

> [GitHub](https://github.com/GaneshajDivekar) | [LinkedIn](https://www.linkedin.com/in/ganesh-divekar-96a72bb7/)

