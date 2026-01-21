# Zootipia with API

Zootipia with API is a Python project that generates a simple animal information website.
The program asks the user for an animal name, fetches data about that animal from an external API, and dynamically creates an HTML website displaying the results.

The project demonstrates how to:
- Work with external APIs
- Process JSON data in Python
- Separate data fetching logic from website generation
- Generate dynamic HTML content using Python

---

## Features

- Fetches animal data from the API Ninjas Animals API
- Asks the user for an animal name via the command line
- Generates an `animals.html` website based on the API response
- Displays a friendly message if the requested animal does not exist
- Clean project architecture with separated data fetcher and website generator

---

## Installation

1. Clone the repository:
   git clone <your-repository-url>
   cd zootipia_with_api

2. Install the required dependencies:
   pip install -r requirements.txt

3. Create a .env file in the root directory and add your API key:
   ANIMALS_API_KEY=your_api_key_here

---

## Usage

To use this project, run the following command - `python main.py`.
