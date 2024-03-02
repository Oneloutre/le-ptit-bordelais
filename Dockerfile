# Start with a build image to install dependencies and compile any extensions
FROM python:3.12-alpine as builder

# Define build-time variable for the bot token
ARG BOT_TOKEN

# Install dependencies in a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the virtual environment into our base image.
FROM python:3.12-alpine
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy the necessary files into the container
COPY ./apis /app/apis
COPY ./Assets /app/Assets
COPY ./connection.py /app/
COPY ./image.jpg /app/
COPY ./main.py /app/
COPY ./requirements.txt /app/

# Set the working directory
WORKDIR /app

# Create a .env file with the bot token
RUN echo "BOT_TOKEN=${BOT_TOKEN}" > .env

# Command to run the script
CMD ["python", "main.py"]
