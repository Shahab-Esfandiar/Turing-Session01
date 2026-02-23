# 🚀 AI Text Engine Pro
**An Advanced Modular Text Processing Suite utilizing Cloud & Local LLMs**

<img width="1918" height="904" alt="image" src="https://github.com/user-attachments/assets/85a213a2-1639-4ce6-b8df-95ba477d88d5" />


This project is a sophisticated AI-powered application designed for high-performance text analysis. It bridges the gap between Cloud-based models (OpenAI) and Local-based models (Ollama), providing a seamless interface for academic and professional text tasks.

---

## 🏗️ System Architecture & Enhancements
Compared to the initial basic version, this project has undergone a complete architectural overhaul to follow **Clean Code** and **SOLID** principles.

### 1. Core Foundations (The "Under the Hood" Upgrades)
* **Client Factory Pattern:** Implemented a `ClientFactory` to decouple the UI from LLM logic. This allows adding new providers (like Anthropic or Gemini) without touching the UI code.
* **Custom Exception Hierarchy:** A specialized error handling system (`core/exceptions.py`) manages service failures, empty inputs, and template errors gracefully.
* **Advanced Logging System:** * **Terminal Logs:** Provides real-time technical metadata (word counts, model names, performance metrics).
    * **Persistent File Logs:** Every transaction is recorded in `app.log` for future debugging.
* **Template-Based Prompting:** Prompts are decoupled into `.txt` files in the `app/prompts/` directory for easy tuning without modifying Python code.

---

## 🛠️ Main Features & Services

### 📝 Summarization Service
* **Dual Model Support:** Choose between OpenAI or Local models (Gemma/Llama).
* **Reading Time Estimation:** Automatically calculates and displays the estimated reading time of the generated summary based on professional WPM standards.
* **Metadata Logging:** Logs original vs. summarized word count ratio in the terminal.

### 🏷️ Text Classification
* **Confidence Scores:** The engine doesn't just categorize; it provides a confidence score (e.g., 0.85) to ensure reliability.
* **Structured Output:** Uses refined prompts to ensure the LLM follows a strict categorization format (Technical, Business, Casual, Legal).

### 🌐 Translation Service (New Feature)
* **Tone Control:** Users can toggle between **Formal** and **Informal** tones, allowing the AI to adjust the vocabulary based on the target audience.
* **Bi-directional Support:** Designed for multi-language flexibility (Default: English to Persian).
* **Char-count Analytics:** Tracks translation expansion/contraction ratios for linguistic analysis.

---

## 💎 UI/UX & Data Features

The system is pre-configured to run optimized local models:
* `gemma3:4b` (Highly efficient for quick tasks)
* `llama3.1:8b` (For deep reasoning and complex analysis)

### 🚩 Professional Data Flagging
A built-in **CSV Logger** allows users to "Flag" high-quality or problematic outputs. 
* Data is saved in `flagged_summarization/`, `flagged_classification/`, and `flagged_translation/`.
* Includes all inputs, outputs, and the specific model used, perfect for building a dataset for fine-tuning.

### ⏱️ Performance Monitoring
* **Clean Timer:** Implemented a minimal progress tracker that counts elapsed time without artificial limits, providing an accurate measure of model inference speed.

---

## 🚀 How to Run

1.  **Clone the Repo**
2.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup Environment:**
    Create a `.env` file and add your `API_KEY` and `BASE_URL`.
4.  **Launch:**
    ```bash
    python main.py
    Running on local URL:  http://127.0.0.1:7860
    ```

---

## 🛠️ Tech Stack
* **Framework:** Gradio (UI)
* **LLM Providers:** OpenAI API & Ollama (Local)
* **Data Management:** Pandas (CSV Logging)
* **Logging:** Python Standard Logging
