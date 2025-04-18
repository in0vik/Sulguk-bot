import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
import sys

# Add sulguk to the path
sys.path.append('./sulguk')

# Import sulguk module
from sulguk import transform_html

# Load environment variables
load_dotenv(override=True)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")
print(BOT_TOKEN)
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN provided")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    """Send a welcome message when the command /start is issued."""
    await message.answer(
        "Hi! 👋 I'm a bot that can format HTML messages for Telegram.\n\n"
        "Send me any HTML text, and I'll convert it into a message with <b>correct</b> Telegram formatting.\n\n"
        "Use /help to see the list of supported tags and an example.",
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )

@dp.message(Command("help"))
async def send_help(message: types.Message):
    """Send a help message when the command /help is issued."""
    help_text = """
<b>Supported HTML tags:</b>

<b>Basic Formatting:</b>
<code>&lt;b&gt;, &lt;strong&gt;</code> → <b>Bold</b>
<code>&lt;i&gt;, &lt;em&gt;, &lt;cite&gt;, &lt;var&gt;</code> → <i>Italic</i>
<code>&lt;u&gt;, &lt;ins&gt;</code> → <u>Underlined</u>
<code>&lt;s&gt;, &lt;strike&gt;, &lt;del&gt;</code> → <s>Strikethrough</s>
<code>&lt;mark&gt;</code> → Marked (<i><b>Bold Italic</b></i>)
<code>&lt;tg-spoiler&gt;</code> or <code>&lt;span class="tg-spoiler"&gt;</code> → Spoiler

<b>Links:</b>
<code>&lt;a href="..."&gt;</code> → <a href="https://telegram.org">Hyperlink</a>

<b>Code:</b>
<code>&lt;code&gt;, &lt;kbd&gt;, &lt;samp&gt;</code> → <code>Inline Monospace</code>
<code>&lt;pre&gt;</code> → <pre>Preformatted block</pre>
<code>&lt;pre&gt;&lt;code class="language-py"&gt;...&lt;/code&gt;&lt;/pre&gt;</code> → Code block with language hint

<b>Lists:</b>
<code>&lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;</code> → Lists (ordered supports <code>start</code>, <code>type</code>, <code>reversed</code>)

<b>Block Elements:</b>
<code>&lt;h1&gt;...&lt;h6&gt;</code> → Headings (styled with bold/italic/underline)
<code>&lt;blockquote&gt;, &lt;details&gt;, &lt;summary&gt;, &lt;dialog&gt;</code> → <blockquote>Blockquote</blockquote>
<code>&lt;p&gt;</code> → Paragraph (adds spacing)
<code>&lt;div&gt;, &lt;section&gt;, etc.</code> → Structural blocks (may add spacing)

<b>Other:</b>
<code>&lt;hr/&gt;</code> → Horizontal rule (empty line)
<code>&lt;br/&gt;</code> → Line break
<code>&lt;img src="..." alt="..."/&gt;</code> → 🖼️ Alt text (linked if src provided)
<code>&lt;progress value=".." max=".."/&gt;</code> → Progress bar (experimental)
<code>&lt;meter value=".." min=".." max=".."/&gt;</code> → Meter bar (experimental)
<code>&lt;tg-emoji emoji-id="..."&gt;text&lt;/tg-emoji&gt;</code> → Custom Telegram Emoji

<b>Example usage:</b>

Just send me HTML code like this:
<code>&lt;h1&gt;Hello!&lt;/h1&gt;&lt;p&gt;This is a &lt;b&gt;test&lt;/b&gt; of &lt;code&gt;sulguk&lt;/code&gt;.&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Item 1&lt;/li&gt;&lt;li&gt;Item 2&lt;/li&gt;&lt;/ul&gt;</code>

I will reply with the formatted message.
"""
    await message.answer(help_text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

@dp.message(Command("example"))
async def send_example(message: types.Message):
    """Send an example HTML message."""
    example_html = """<h1>This is a Sulguk Example</h1>
<p>This library helps with <b>formatting</b> <i>messages</i> in <u>Telegram</u>.</p>
<blockquote>It's really useful!</blockquote>
<ol>
    <li>Supports lists</li>
    <li>And <a href="https://telegram.org">links</a></li>
    <li>And much more!</li>
</ol>"""
    
    result = transform_html(example_html)
    
    await message.answer(
        text=result.text,
        entities=result.entities,
        disable_web_page_preview=True
    )

@dp.message(F.text)
async def process_html(message: types.Message):
    """Process HTML text sent by the user."""
    try:
        # Replace spaces with non-breaking spaces and preserve line breaks
        processed_text = message.text.replace("\n", "<br/>")
        result = transform_html(processed_text)
        
        await message.answer(
            text=result.text,
            entities=result.entities,
            disable_web_page_preview=True
        )
    except Exception as e:
        await message.answer(f"Error processing your HTML: {str(e)}", disable_web_page_preview=True)

async def main():
    # Start the bot
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 