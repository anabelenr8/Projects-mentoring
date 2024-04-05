## Table of Contents

1. [Description](#description)
1. [Demo](#demo)
1. [Design](#design)
1. [Features](#features)
1. [Technologies Used](#technologies-used)
1. [Project Challenges](#project-challenges)
1. [Thoughts and Observations](#thoughts-and-observations)
1. [Future Enhancements](#future-enhancements)
1. [Installation](#installation)

<br>

## Description

<br>

## Demo

Provide a link to a live demo.

It's best to use a real domain, like `https://yourname.com/api/docs`.<br>

- Use a link to API docs if you're mainly focusing on Python+Django API development.
- Use a link to a landing page if you have frontend.

<br>

Adjust "Click here" link below:

<br>

Click here: [https://link-to-your-demo-goes-here/](https://link-to-your-demo-goes-here/)

<br>

## Design

Add a screenshot or video here.

- I recommend https://loom.com/ for video.
- I recommend https://www.digitalocean.com/products/spaces for any files.

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

- Survey Submission Endpoint: A POST endpoint (post_report_generation) that accepts survey responses related to a user's
  fashion preferences, including questions on personal style, preferred color palettes, shopping categories, sizing
  preferences, and attitudes towards recycling and sustainability in fashion. The endpoint validates incoming data,
  processes the survey responses, and generates a personalized report based on the user's inputs.


- Survey Retrieval Endpoint: A GET endpoint (get_api_survey_and_answers) designed to fetch the survey questions and
  possible answers for users to select from. This endpoint aids in dynamically generating the survey UI, presenting
  options on personal style, color preferences, shopping behavior, measurement standards, and views on recycled
  materials.

<br>

## Technologies Used

- Django & Django Rest Framework: Leveraged for backend infrastructure, providing a powerful toolkit for building web
  APIs.
- DRF-YASG: Used for generating Swagger/OpenAPI 2.0 documentation for the Django Rest Framework API, enhancing developer
  experience and endpoint discoverability.

<br>

## Project Challenges

Discuss any challenges you faced during the project's development, including how you overcame them or what you learned
from these experiences.

<br>

## Thoughts and Observations

Share any insights or reflections you have from working on the project. This could include your thoughts on the
development process, design decisions etc.

<br>

## Future Enhancements

Outline any potential improvements or features you might want to add in the future. This shows the project's potential
for growth and areas for further development.

<br>

## Installation

Provide instructions on how to install and run your project locally.

Example below:

1. Clone the GitHub repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-project-name.git
   ```

2. Navigate to the project's directory:

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