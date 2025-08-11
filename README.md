# 🤖 Agentic AI Project 5: AI Interviewer

![Python](https://img.shields.io/badge/Python-3.12%2B-brightgreen)
![Agentic AI](https://img.shields.io/badge/Agentic%20AI-Interviewer-blue)
![AI Interview](https://img.shields.io/badge/AI-Interview-orange)
![License](https://img.shields.io/badge/License-GPL--3.0-orange)

A cutting-edge, agentic, end-to-end AI-powered interviewer platform. This project leverages modular agent design and advanced LLMs to simulate realistic, adaptive interview sessions for candidates in various domains. Built for extensibility, research, and practical mock interview workflows.

> 📁 **Repository:** `Agentic_AI_Project5_AI_Interviewer`

---

## 🚀 Project Highlights

- 💬 **AI Interview Simulation:**  
  Conducts realistic, interactive interview sessions using LLMs as interviewer agents.
- 🤖 **Agentic AI Design:**  
  Modular components for easy extension—add new question styles, evaluation metrics, or interview flows.
- 🧠 **Adaptive Questioning:**  
  Dynamically adjusts questions based on candidate responses.
- 📈 **Performance Feedback:**  
  Can be extended to provide scores, feedback, and improvement suggestions.
- 🧩 **Extensible:**  
  Integrate new domains, roles, or interview strategies quickly.

---

## 🧠 Technical Stack

- **Python 3.12+**
- **Agentic AI Patterns**
- **LLMs for conversation and evaluation**
- **Modular agent, node, and tool abstractions**

---

## 🏗️ Project Structure

```bash
Agentic_AI_Project5_AI_Interviewer/
├── AI_interview.py             # Main AI interviewer logic
├── 0. AI Interview using Autogen.ipynb   # Jupyter notebook demo
├── interview_simulator.cpython-312.pyc   # Compiled/intermediate files
├── AI_interview.cpython-312.pyc
├── main.py                    # Alternate entry point
├── requirements.txt
├── LICENSE
├── README.md
├── Project Structure.excalidraw # Visual project structure
└── __pycache__/
```

---

## ⚡ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdzaheerjk/Agentic_AI_Project5_AI_Interviewer.git
cd Agentic_AI_Project5_AI_Interviewer
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the AI Interviewer
```bash
python AI_interview.py
```
or (for the notebook demo):
```bash
jupyter notebook "0. AI Interview using Autogen.ipynb"
```
or (alternate entry):
```bash
python main.py
```

---

## 🧪 Example Usage

- **Run a Mock Interview:**  
  Start the application and follow prompts for a simulated interview experience.
- **Jupyter Demo:**  
  Explore and interact with the notebook for step-by-step mock interviews.
- **Extend Easily:**  
  Add new interview question modules, feedback agents, or evaluation criteria.

---

## 🧩 Extensibility

- **Add Interview Domains:**  
  Introduce new roles (tech, HR, etc.) by adding question sets or agents.
- **Custom Feedback:**  
  Enhance with automatic scoring, resume analysis, or personalized feedback.

---

## 📚 Documentation

See comments in source files for extension instructions and workflow details.

---

## ✍️ Author

**Mohammed Zaheeruddin**  
🎓 First-Year B.Tech Student | AI/ML & GenAI Enthusiast  
🏫 Shetty Institute of Technology, Gulbarga  
📧 info.zaheerjk@gmail.com

---

## 📜 License

This project is licensed under the **GPL-3.0 License** – see the LICENSE file for details.

---

#### Key Features:
1. Realistic, LLM-powered AI interviewer simulations
2. Modular, extensible codebase for new domains and interview types
3. Easy integration of feedback, scoring, and analytics
4. Designed for research, learning, and real-world mock interview pipelines
