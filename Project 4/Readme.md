# Chat Bot Readme

This simple Python script implements a basic chat bot that interacts with users by responding to their input based on pre-defined knowledge stored in a JSON file. The bot utilizes the `difflib` library to find the closest matching question in the knowledge base to the user's input.

## How to Use

### Prerequisites

- Python 3.x
- Knowledge base JSON file (`knowledge_base.json`) with pre-defined questions and answers.

### Installation

1. Clone the repository or download the script (`chat_bot.py`).
2. Ensure you have a knowledge base JSON file named `knowledge_base.json` in the same directory as the script.

### Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script and the `knowledge_base.json` file.
3. Run the script by executing `python chat_bot.py`.
4. Start interacting with the chat bot by typing your questions or input.
5. Type `quit` to exit the chat bot.

## Script Overview

- `load_knowledge_base(file_path: str) -> dict`: Function to load the knowledge base from a JSON file.
- `save_knowledge_base(file_path: str, data: dict)`: Function to save the knowledge base to a JSON file.
- `find_best_match(user_question: str, questions: list[str]) -> str | None`: Function to find the best matching question in the knowledge base for a user input.
- `get_answer_for_question(question: str, knowledge_base: dict) -> str | None`: Function to retrieve the answer for a given question from the knowledge base.
- `chat_bot()`: Main function implementing the chat bot's interaction logic.

## Customization

You can customize the behavior of the chat bot by modifying the knowledge base JSON file (`knowledge_base.json`). Add or remove questions and answers as needed to improve the bot's responses.

## Dependencies

- Python 3.x
- `difflib` library (built-in)
  
## Output Sample

![image](https://github.com/Anuragkumar23/Intermediate_Tasks/assets/72218283/7c3edae2-756d-492e-bdb2-bede8f1f89e4)


## License

This script is provided under the [MIT License](LICENSE).
