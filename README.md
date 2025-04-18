# Telegram HTML Formatting Bot

A simple Telegram bot that uses the [Sulguk](https://github.com/tishka17/sulguk) library to format HTML messages in Telegram.

## Features

- Format HTML messages into Telegram's native formatting
- Support for a wide range of HTML tags
- Simple to use and deploy

## Setup and Installation

### Local Development

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/tg-html-bot.git
   cd tg-html-bot
   ```

2. Clone the Sulguk library (develop branch):

   ```
   git clone --branch develop https://github.com/tishka17/sulguk.git
   ```

3. Create a virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Create a `.env` file from the example:

   ```
   cp .env.example .env
   ```

5. Edit the `.env` file and add your Telegram bot token (obtained from [@BotFather](https://t.me/BotFather))

6. Run the bot:
   ```
   python main.py
   ```

### Deployment to Google Cloud Run

1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

2. Authenticate with Google Cloud:

   ```
   gcloud auth login
   ```

3. Create a new project or select an existing one:

   ```
   gcloud projects create [PROJECT_ID]
   gcloud config set project [PROJECT_ID]
   ```

4. Enable the necessary APIs:

   ```
   gcloud services enable cloudbuild.googleapis.com run.googleapis.com
   ```

5. Build and deploy the container:

   ```
   gcloud builds submit --tag gcr.io/[PROJECT_ID]/tg-html-bot
   ```

6. Deploy to Cloud Run:
   ```
   gcloud run deploy tg-html-bot \
     --image gcr.io/[PROJECT_ID]/tg-html-bot \
     --platform managed \
     --allow-unauthenticated \
     --update-env-vars BOT_TOKEN=your_telegram_bot_token
   ```

## Bot Commands

- `/start` - Start the bot
- `/help` - Get help on how to use the bot
- `/example` - See an example of HTML formatting

## Usage

Simply send any HTML text to the bot, and it will format it according to Telegram's entity system.

Example:

```html
<h1>Hello World</h1>
<p>This is a <b>bold</b> and <i>italic</i> text.</p>
<blockquote>This is a quote</blockquote>
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
