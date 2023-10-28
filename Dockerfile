# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container 
COPY . .

# Install dependencies
RUN pip install -r requirements.txt


# Define environment variable
ENV WEBHOOK_URL=https://discord.com/api/webhooks/1162322646021714040/zeTDFjHnly0NZRfpU_hG_GTomnARmXJMVpzUYdjzHWnkXfFbQBEmaCr4k4vjcVyB4HLi

# Run the script
CMD [ "python", "get_pic.py" ]

