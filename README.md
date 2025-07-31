# Telegram Mini App - FastAPI Template

A modern, production-ready Telegram Mini App template built with FastAPI, featuring a complete bot integration and beautiful web interface.

## 🚀 Features

- **FastAPI Backend**: High-performance async API with automatic documentation
- **Telegram Bot Integration**: Complete bot with Mini App support
- **Modern UI**: Responsive design with Telegram theme integration
- **Security**: HMAC validation for Telegram data
- **User Management**: Automatic user data extraction and display
- **Message System**: Send messages through the Mini App
- **Theme Support**: Automatic dark/light mode adaptation
- **CORS Support**: Proper cross-origin configuration
- **Health Checks**: Built-in monitoring endpoints

## 📋 Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (get from [@BotFather](https://t.me/BotFather))
- Web server or hosting service (for production)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/telegram-mini-app-fastapi.git
   cd telegram-mini-app-fastapi
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` file with your configuration:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   WEBAPP_URL=https://your-domain.com
   PORT=8000
   HOST=0.0.0.0
   DEBUG=True
   ```

5. **Create a Telegram Bot**
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Use `/newbot` command to create a new bot
   - Copy the bot token to your `.env` file

## 🚀 Running the Application

### Development Mode

1. **Start the FastAPI web server**
   ```bash
   python minimal_app.py
   ```
   The API will be available at `http://localhost:8000`

2. **Start the Telegram bot** (in a separate terminal)
   ```bash
   python bot.py
   ```

### Production Deployment

1. **Deploy to your hosting service** (Heroku, Railway, DigitalOcean, etc.)
2. **Set environment variables** on your hosting platform
3. **Update the WEBAPP_URL** in your `.env` file to your production domain
4. **Run the bot** on your server or use a service like Railway

## 📱 Using the Mini App

1. **Start the bot** by sending `/start` to your bot
2. **Click "Open Mini App"** button in the bot's response
3. **Interact with the Mini App** interface
4. **Send messages** and perform actions within the app

## 🏗️ Project Structure

```
telegram-mini-app-fastapi/
├── minimal_app.py          # Minimal FastAPI application
├── app.py                  # Full FastAPI application with templates
├── bot.py                  # Telegram bot handler
├── requirements.txt        # Python dependencies
├── env.example            # Environment variables template
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── templates/
│   └── index.html         # Main Mini App interface
└── venv/                  # Virtual environment
```

## 🔧 Configuration

### Environment Variables

- `BOT_TOKEN`: Your Telegram bot token from @BotFather
- `WEBAPP_URL`: The URL where your Mini App is hosted
- `PORT`: Port number for the FastAPI server (default: 8000)
- `HOST`: Host address for the server (default: 0.0.0.0)
- `DEBUG`: Enable/disable debug mode

### Telegram Bot Setup

1. **Create a bot** with @BotFather
2. **Set bot commands** (optional):
   ```
   start - Open the Mini App
   help - Show help information
   info - Show bot information
   ```
3. **Configure Mini App** in @BotFather:
   - Use `/newapp` command
   - Set your web app URL
   - Configure app settings

## 🔒 Security Features

- **HMAC Validation**: All Telegram data is validated using HMAC-SHA256
- **Data Verification**: User data is verified before processing
- **CORS Support**: Proper CORS configuration for web requests
- **Environment Variables**: Sensitive data stored in environment variables

## 📡 API Endpoints

### Minimal App (`minimal_app.py`)
- `GET /` - Root endpoint with API status
- `GET /health` - Health check endpoint
- `POST /api/send-message` - Send message to user
- `GET /api/info` - API information
- `GET /docs` - Interactive API documentation

### Full App (`app.py`)
- `GET /` - Main Mini App interface
- `POST /api/init` - Initialize Mini App with Telegram data
- `POST /api/send-message` - Send message to user
- `GET /api/user-data` - Get user information
- `GET /health` - Health check endpoint
- `GET /api/info` - API information

## 🎨 Customization

### Styling
The Mini App uses Telegram's CSS variables for theming:
- `--tg-theme-bg-color`: Background color
- `--tg-theme-text-color`: Text color
- `--tg-theme-button-color`: Button color
- `--tg-theme-hint-color`: Hint text color

### Adding Features
1. **New API endpoints**: Add routes in `minimal_app.py` or `app.py`
2. **Bot commands**: Add handlers in `bot.py`
3. **UI components**: Modify `templates/index.html`
4. **Database integration**: Add database models and connections

## 🐛 Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check if bot token is correct
   - Ensure bot is running (`python bot.py`)

2. **Mini App not loading**
   - Verify WEBAPP_URL is correct
   - Check if FastAPI server is running
   - Ensure HTTPS is used in production

3. **Data validation errors**
   - Check bot token configuration
   - Verify HMAC validation logic

4. **CORS errors**
   - Ensure CORS is properly configured
   - Check domain settings

### Debug Mode

Enable debug mode for detailed error messages:
```env
DEBUG=True
```

## 📚 Resources

- [Telegram Mini Apps Documentation](https://core.telegram.org/bots/webapps)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the documentation
3. Open an issue on GitHub

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/telegram-mini-app-fastapi&type=Date)](https://star-history.com/#yourusername/telegram-mini-app-fastapi&Date)

---

**Happy coding! 🚀**

Made with ❤️ using FastAPI and Telegram Bot API 