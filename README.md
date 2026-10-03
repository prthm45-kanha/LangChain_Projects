# LangChain Projects

Welcome to the LangChain Projects repository! This repository contains various scripts, notebooks, and experiments demonstrating how to use [LangChain](https://github.com/langchain-ai/langchain) with different Large Language Models (LLMs) and tools.

## Contents

- **Jupyter Notebooks (`updatedlangchain/`)**: A series of tutorials covering LangChain basics:
  - Introduction to LangChain
  - Model Integration
  - Using Tools and Agents
  - Message Handling
  - Structured Output Parsing
- **Testing Scripts**: Various Python scripts testing integrations with different models and providers:
  - Google Gemini (`test_gemini.py`)
  - Groq (`test_groq_*.py`) with models like Llama 3 (70B), Gemma, Mixtral, and Qwen.
  - Tool calling and system prompts testing.
- **Dependency Management**: Uses `pyproject.toml`, `requirements.txt`, and `uv` for managing dependencies.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prthm45-kanha/LangChain_Projects.git
   cd LangChain_Projects
   ```

2. **Install dependencies:**
   You can install the required dependencies using `pip` or `uv`:
   ```bash
   pip install -r requirements.txt
   ```
   *or if you are using `uv`:*
   ```bash
   uv sync
   ```

3. **Set up Environment Variables:**
   You will need API keys for the providers you wish to test (e.g., `GROQ_API_KEY`, `GOOGLE_API_KEY`). You can set these in your environment or a `.env` file.

4. **Run the Notebooks:**
   Start Jupyter to explore the notebooks in the `updatedlangchain/` directory:
   ```bash
   jupyter notebook
   ```

## License
[MIT](LICENSE)
