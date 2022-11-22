FROM python:3.10.8

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install playwright dependencies
RUN playwright install