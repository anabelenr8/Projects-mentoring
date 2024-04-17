## Table of Contents

1. [Description](#description)
1. [Demo](#demo)
1. [Design](#design)
1. [Features](#features)
1. [Technologies Used](#technologies-used)
1. [Thoughts and Observations](#thoughts-and-observations)
1. [Future Enhancements](#future-enhancements)
1. [Installation](#installation)

<br>

## Description

The "Style and Sustainability Survey Report" is a Django-based REST API project
designed to collect users' preferences on fashion and sustainability. Users are
queried on their style, color palette, shopping habits, garment size, and views
on recycling materials. This project aims to gather insights for a
fashion brand to tailor their offerings and sustainability practices more
closely to customer preferences.

<br>

## Demo

A live demo of the API is available. The Swagger documentation provides a
comprehensive guide on how to interact with the API endpoints, including
submitting survey responses and retrieving aggregated data.

<br>

Adjust "Click here" link below:

<br>

Click
here: [https://link-to-your-demo-goes-here/](https://link-to-your-demo-goes-here/)

<br>

## Design TBC

The application design follows a microservice architecture, with the Django
REST framework facilitating the creation of a clean, RESTful API. The project
structure emphasizes modularity, allowing easy extension or modification of
survey questions and processing logic.

<br>

<p align="center">
  <img src="https://robertsgreibers.sfo3.cdn.digitaloceanspaces.com/mentoring/m6-readme-file-example-1.png" width="750px" />
</p>

<br>

<p align="center">
  <img src="https://robertsgreibers.sfo3.cdn.digitaloceanspaces.com/mentoring/m6-readme-file-example-2.png" width="750px" />
</p>

<br>

## Features

- Dynamic survey endpoints that accept varied user inputs on fashion and
  sustainability.
- Detailed Swagger documentation for ease of API interaction.
- Modular design for straightforward updates to survey content or logic.
- Persistent storage of survey responses for future analysis.

<br>

## Technologies Used

- Django & Django REST Framework for the backend API.
- Swagger for API documentation.
- Git for version control.

<br>

## Thoughts and Observations

Working on this project highlighted the importance of clear API documentation
and the challenges of designing a database schema that can handle a variety of
data types and structures efficiently.

<br>

## Future Enhancements

- Implementing authentication to manage user sessions and personalize the
  survey experience.
- Adding machine learning algorithms to analyze survey responses for trends.
- Enhancing the API to support real-time data analytics.

<br>

## Installation

Provide instructions on how to install and run your project locally.

Example below:

1. Clone the GitHub repository to your local machine: TBD

   ```bash
   git clone https://github.com/your-username/your-project-name.git
   ```

2. Navigate to the project's directory: TBD

   ```bash
   cd your-project-name
   ```

3. Install the project's dependencies using pipenv:

   ```bash
   pipenv install
   ```

4. To start the project server:

   ```bash
   python manage.py runserver
   ```

<br>
<br>