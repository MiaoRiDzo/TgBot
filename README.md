# Equipment Tracker Bot

**Equipment Tracker Bot** is a Telegram bot designed to track the status and location of various equipment. This bot allows users to manage equipment details, monitor their status, and track their location easily through a Telegram interface.

## Features

- Add and manage equipment details
- Track the status of equipment
- Monitor the location of equipment
- Manage user requests related to equipment

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/equipment-tracker-bot.git
    cd equipment-tracker-bot
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```python
    from models import Base, engine
    Base.metadata.create_all(engine)
    ```

5. **Configure the bot token**:
    - Create a file named `config.py` and add your Telegram bot token:
        ```python
        TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'
        ```

6. **Run the bot**:
    ```bash
    python bot.py
    ```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
