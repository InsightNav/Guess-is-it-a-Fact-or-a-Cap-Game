# Fact or Cap Game 🎮

A CLI game where you try to spot the real fact among believable fakes.

The game leverages AI to dynamically generate content, with a fallback system to ensure uninterrupted gameplay even when API access is unavailable.

---

## Features

- AI-generated fact vs fiction pairs
- Support for multiple AI providers (Gemini, OpenAI, Claude)
- Pluggable architecture for easy provider switching
- Built-in fallback dataset for offline play
- Score and streak tracking
- Lightweight and terminal-based

---

## Parts Made with the help of ai

fallback library

few logical decisions

few ui elements

fallback system(with detailed prompt and planning)

## Installation

Clone the repository:

```bash
git clone [https://github.com/your-username/fact-or-cap.git
cd fact-or-cap](https://github.com/InsightNav/Guess-is-it-a-Fact-or-a-Cap-Game/tree/main?tab=readme-ov-file)
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Configuration

Create a .env file in the project root:
>
>AI_PROVIDER=gemini
>
>GEMINI_API_KEY=your_key_here
>
>OPENAI_API_KEY=your_key_here
>
>CLAUDE_API_KEY=your_key_here
>

## Usage

Run the game:
```
python main.py
```
Follow the on-screen prompts to select the correct statement.

## Switching AI Providers

The project is designed to be provider-agnostic.

To switch providers, update the following in .env:
>
>AI_PROVIDER=openai
>
Supported values:
>
>- gemini
>
>- openai
>
>- claude
>

No other code changes are required

## Fallback Behavior

If an API request fails (e.g., rate limits, missing quota, invalid key), the system automatically falls back to a local dataset.

This ensures:

- zero runtime crashes

- consistent gameplay without API dependency

## Design Notes

- The AI layer is abstracted to isolate external dependencies

- Minimal coupling between game logic and provider implementation

- Easy to extend with additional providers or custom models

## Possible Improvements

- Difficulty scaling based on streak

- Categorized questions (science, history, etc.)

- Persistent leaderboard

- Multiple mode(online/offline)

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome. Feel free to fork or copy the repo and submit a pull request.

## THANKYOU Built for fun, designed with flexibility 
