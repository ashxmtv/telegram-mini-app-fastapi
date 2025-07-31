import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = os.getenv('WEBAPP_URL', 'https://your-domain.com')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that opens the Mini App."""
    keyboard = [
        [InlineKeyboardButton(
            "🚀 Open Mini App", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to the Telegram Mini App!\n\n"
        "Click the button below to open the Mini App:",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message."""
    help_text = """
🤖 **Telegram Mini App Bot Commands:**

/start - Open the Mini App
/help - Show this help message
/info - Show bot information

**Features:**
• Interactive Mini App interface
• User data integration
• Message sending capabilities
• Theme-aware UI
• FastAPI backend

**How to use:**
1. Click the "Open Mini App" button
2. Interact with the app interface
3. Send messages and perform actions
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show bot information."""
    user = update.effective_user
    info_text = f"""
📊 **Bot Information:**

**User Details:**
• Name: {user.first_name} {user.last_name or ''}
• Username: @{user.username or 'None'}
• User ID: {user.id}

**Bot Details:**
• Mini App URL: {WEBAPP_URL}
• Backend: FastAPI
• Status: Active ✅

**Commands Available:**
• /start - Open Mini App
• /help - Show help
• /info - Show this info
    """
    
    await update.message.reply_text(info_text, parse_mode='Markdown')

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle data received from the Mini App."""
    try:
        # Get data from the Mini App
        data = update.effective_message.web_app_data.data
        logger.info(f"Received web app data: {data}")
        
        # You can process the data here
        # For example, save to database, send notifications, etc.
        
        await update.message.reply_text(
            f"✅ Data received from Mini App!\n\n"
            f"Data: {data[:100]}{'...' if len(data) > 100 else ''}"
        )
        
    except Exception as e:
        logger.error(f"Error handling web app data: {e}")
        await update.message.reply_text("❌ Error processing Mini App data")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("No bot token provided. Please set BOT_TOKEN in your .env file")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot
    logger.info("Starting Telegram Mini App Bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 