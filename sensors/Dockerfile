FROM python:3.8-slim-buster

# Create a working directory.
RUN mkdir wd
WORKDIR wd

# Install Python dependencies.
COPY ./sensors/requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the script.
COPY ./sensors/mysensor.py ./sensors/mysensor.py

# Finally, run the script.
CMD ["python3", "sensors/mysensor.py"]
