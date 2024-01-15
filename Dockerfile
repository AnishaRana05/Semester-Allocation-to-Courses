# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /allocation-image

# Copy the Python scripts into the container
COPY ./ /allocation-image/

# Run main.py when the container launches
CMD ["python", "main.py"]
#terminal
#docker image build -t allocation-app:1.0 ./
#docker tag allocation-app:1.0 anisharana/allocation-app:1.0


