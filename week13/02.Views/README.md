# Course Management System Views

We'll now create views for the models from the last exercise.

## Index view

- `GET /` There should be an index view with a navigation to all list views.

## Courses views

For our courses, we should have the following HTML views:

- `GET /courses` should display a nice table with all courses, sorted by their start date. The table should look like this:

| Course Name                 | Description | Start Date | End Date   | Duration |
| --------------------------- | ----------- | ---------- | ---------- | -------- |
| Programming 101 with Python | Python!     | 01.01.2016 | 01.03.2016 | 3 months |
| Programming 101 with Ruby   | Ruby.       | 10.01.2016 | 01.03.2016 | 2 months |

The course name should be a link to the course detail page.

- `GET /courses/<course_id>/` - this is the detailed course page. Add a list of all lectures for the given course with a link to the detail view of the lecture.
- `GET /courses/new/` - this should display a form for creating new course.
- `POST /courses/new/` - this should be handled by Django for creating new courses.
- `GET /courses/<course_id>/edit/` - this should display a form to edit some of the course details.
- `PUT /courses/edit/<course_id>/edit/` - this should be handled by Django for editing existing courses.

## Lectures views

We should have a set of URLs for creating and editing lectures:

- `GET /lectures` should display a list of all lectures grouped by their course
- `GET /lectures/<lecture-id>` should display (in a table) the information for our lecture. Should have a link to the related course.
- `GET /lectures/new` - the form for creating a new lecture
- `POST /lectures/new` - handled by Django for saving the lecture
- `GET /lectures/<lecture-id>/edit` - the form for editing an existing lecture
- `PUT /lectures/<lecture-id>/edit` - handled by Django for editing an existing lecture
