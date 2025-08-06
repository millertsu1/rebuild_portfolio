# My Portfolio

This is a personal portfolio website built with Python and Django.

## Features

*   Displays personal information, projects, and experience.
*   Uses CKEditor for rich text editing of content.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3
*   pip (Python package installer)

### Installation

1.  Clone the repository:
    ```bash
    git clone <your-repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd NwePortfolio
    ```
3.  Create a virtual environment:
    ```bash
    python -m venv env
    ```
4.  Activate the virtual environment:
    *   **Windows:**
        ```bash
        env\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source env/bin/activate
        ```
5.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the application

1.  Navigate to the `rebuild_portfolio` directory:
    ```bash
    cd rebuild_portfolio
    ```
2.  Apply the database migrations:
    ```bash
    python manage.py migrate
    ```
3.  Start the development server:
    ```bash
    python manage.py runserver
    ```
4.  Open your web browser and go to `http://127.0.0.1:8000/`
