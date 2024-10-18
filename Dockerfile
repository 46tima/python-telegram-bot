# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY bot.py .

# Set environment variable for token
ENV TELEGRAM_TOKEN=YOUR_BOT_TOKEN

# Run the bot
CMD ["python", "bot.py"]
