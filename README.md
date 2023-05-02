# Chitkara Mess Bot

This is a simple Python script for a Telegram bot that reminds users about the menu for the day in Chitkara Mess. It uses the `telebot` library to interact with the Telegram Bot API.

## How to use

To use this bot, you need to have a Telegram account and create a new bot using the [BotFather](https://core.telegram.org/bots#6-botfather) bot. Once you have created a bot, copy the API token and paste it in the `API_KEY` variable in the script.

To run the script, you can execute the following command:

```
python bot.py
```

This will start the bot and it will be ready to receive commands.

## Available commands

The bot supports the following commands:

- `/start` or `/hello`: Sends a welcome message to the user.
- `/breakfast`: Displays the breakfast menu for the day.
- `/lunch`: Displays the lunch menu for the day.
- `/snacks`: Displays the snacks menu for the day.
- `/dinner`: Displays the dinner menu for the day.

## Menu data

The menu data is stored in the following lists:

- `breakfast`
- `lunch`
- `snacks`
- `dinner`

Each list contains a string with the menu for a specific day of the week. The bot uses the `datetime` module to get the current day of the week and display the corresponding menu.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.
