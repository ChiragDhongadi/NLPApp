# NLPApp

A user-friendly Python desktop application built with Tkinter that allows users to register, login, and perform essential Natural Language Processing tasks: Sentiment Analysis, Named Entity Recognition (NER), and Language Detection.

---

##  Features

- **User Authentication**  
  Register new users and securely log in with email and password (data stored in `db.json`) :contentReference[oaicite:2]{index=2}.

- **Sentiment Analysis**  
  Analyze text to determine sentiment categories.

- **Named Entity Recognition (NER)**  
  Identify and classify entities such as people, organizations, and locations.

- **Language Detection**  
  Detect the language of the entered text.

---

##  Screenshot

![App Screenshot](https://picsart.onelink.me/VgrZ/bxkn1rwj)  
*(Replace with your actual screenshot file path.)*

---

##  Repository Structure
NLPApp/
│
├── app.py # Main GUI logic: login/register/home/sentiment layout
├── myapi.py # Module handling NLP API calls
├── mydb.py # Database interactions (user registration & login)
├── db.json # JSON file used to store user credentials
├── resources/ # Contains assets like app icons or screenshots
└── README.md # Project documentation


---

##  Installation & Usage

### Prerequisites

- Python 3.7+
- Tkinter (usually included with Python)
- Any required packages listed in `requirements.txt` (if present)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ChiragDhongadi/NLPApp.git
   cd NLPApp

````markdown
2. **(Optional) Create and activate a virtual environment**

   **Mac/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
````

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies** (if you have a `requirements.txt` file)

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

