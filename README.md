# Currency Exchange Rate Telegram Bot

This project is a Telegram bot that provides users with real-time currency exchange rates from PrivatBank. 

## Features

- **Start Conversation**: Initiates a conversation with the bot where users can request the current exchange rate.
- **Get Exchange Rates**: Provides up-to-date exchange rates from PrivatBank when users select the relevant option.
- **Easy Integration**: Built using Python's `python-telegram-bot` library for seamless integration with Telegram's API.
- **Customizable Commands**: Easy to expand with additional commands or features.
- **Keyboard Integration**: Includes a reply keyboard for easy user interaction.

## Requirements

- Python 3.12
- A valid Telegram bot token

### Python Libraries

The following Python libraries are used in the project:

- `python-telegram-bot`: For creating and managing the Telegram bot.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `httpx`: Used internally for making HTTP requests to retrieve exchange rates (configured to avoid excessive logging).
- `os`: For accessing environment variables.
- `logging`: For logging events and errors.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/telegram-currency-bot.git
    cd telegram-currency-bot
    ```

2. **Install required dependencies**:
    Make sure you have `pip` installed, and then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment variables**:
    Create a `.env` file in the project directory with your Telegram bot token:
    ```bash
    BOT_TOKEN=your-telegram-bot-token
    ```

4. **Run the bot**:
    Start the bot by running the following command:
    ```bash
    python bot.py
    ```

## How to Use

1. **Start the bot**: Open Telegram and send the `/start` command to the bot.
2. **Get Exchange Rates**: Press the **Get the currency exchange rate** button from the keyboard to receive the current rates from PrivatBank.

## Project Structure

- `bot.py`: The main bot logic, handling conversations and user interactions.
- `utilities.py`: Contains utility functions like `get_rate()` to fetch currency rates and `form_massage()` to format messages for display.
- `.env`: Environment variables, including the bot token.
- `requirements.txt`: Python package dependencies.

## Customization

You can add more commands or features by modifying the conversation handler in `bot.py` and extending the keyboard with new options. For example, you could add functionality to check different banks or exchange rates for other currencies.
