markdown
Copy code
# Real-Time Weather Data Assignment

This project retrieves real-time weather data, processes it, and provides visualizations and alerts based on user-configurable thresholds. The tech stack includes Django, Django Rest Framework, Python, React, ECharts, Celery, and Celery Beat.

## Tech Stack

- **Backend:** Django, Django Rest Framework, Python
- **Frontend:** React, ECharts
- **Task Queue:** Celery, Celery Beat

## Features

- Retrieves weather data from the OpenWeatherMap API.
- Processes and calculates daily weather summaries.
- Triggers alerts based on user-defined thresholds.
- Supports visualizations for weather summaries, trends, and alerts.

## Installation

### Clone the Project
    git clone <repository-url>
    cd <project-directory>

### Install Dependencies
    pip install -r requirements.txt

### Run redis on localhost on this port 6379

### Run Project
    python manage.py runserver

### Run celery on different terimal
    celery -A core.celery worker --pool=solo -l info

### Run celery beat on different terimal
    celery -A core beat -l info

## Setup frontend also:
[Frontend Repo link](https://github.com/Aman16-ai/realtime-weather-client)