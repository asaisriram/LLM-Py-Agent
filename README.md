# LLM Py Agent

A sample Python-based AI Agent with a GUI built with CustomTkinter and powered by the GenAI API.

- GUI: Interface for Input prompt and output display using python lib CustomTkinter.
- YAML Configuration: Manage model names, temperatures, and debug modes outside of the code.
- Debug Mode: To test project changes without consuming API tokens.

# Project Structure

LLM_PY_AGENT/
├── src/
│   ├── agent.py          # Gemini API logic & mocking
│   ├── gui.py            # CustomTkinter interface
│   └── utils.py          # Utilities such as YAML configuration handler
├── main.py               # Entry point & bridge
├── projectConfig.yaml    # Application settings
├── .env                  # API Keys (Ignored by Git)
└── pyproject.toml        # Dependency management via uv