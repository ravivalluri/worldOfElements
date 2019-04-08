# Elements Catalog

To view locally clone the repo, download the requirements with
`pip install -r requirements.txt`
`python manage.py migrate`
`python manage.py runserver`.

## Description

The home page of the site contains a list of all of the elements in a database. Clicking on a element’s name opens a page that displays information about the element.

## User Stories

- As a user, I should be able to to filter elements by first letter in element name, grouping, and category.
- As a user, I should be able to user the search bar to perform a full-text search of the app.
- As a user, I should be able to view a random element page by clicking a button.
- As a user, I should be able to seed a database with the elements.json file.

## Completed Development Tasks

- Write a model to store the element data. Write a script that constructs a element model instance for each element in
  elements.json and saves them to a SQLite database.
- Create a layout template for the app.
- Create a template and view to show the names of all the elements.
- Create a element details template and view.
- Write unit tests to test that models, classes, and other functions are working correctly.
- Add css throughout the app to make changes match provided files.
- Queries to the database should be optimized and take no longer than 10ms to complete.
- Complete above user stories.
