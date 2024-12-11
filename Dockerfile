# Start with a base Ubuntu image and install Python
FROM ubuntu:22.04

# Avoid prompts from apt
ARG DEBIAN_FRONTEND=noninteractive

# Install Python and other dependencies, and apply updates
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3-pip python3-dev python3-venv git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install build tools to support modern Python packaging
RUN pip install --no-cache-dir --upgrade pip setuptools wheel build

# Set the working directory in the container
WORKDIR /usr/src/app

# Clone the repository
RUN git clone --branch container https://github.com/AlexandrovLab/SigProfilerToolkit.git .

# Ensure pyproject.toml is used for the build
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --use-pep517 .

# Create a non-root user named 'spm_user'
RUN useradd -m -s /bin/bash spm_user

# Change the ownership of the /usr/src/app directory and its contents to the new non-root user
RUN chown -R spm_user:spm_user /usr/src/app

# Switch to the non-root user for subsequent commands and when running the container
USER spm_user

# Set the default command to run when the container starts
ENTRYPOINT ["SigProfilerToolkit"]
