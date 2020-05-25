# Hackademy

We are going to implement a simple course management system to hold courses & lectures.

Make a fresh Django app.

The model specification is as follows:

## Courses

First of all, our system should know about courses.

We are interested in the following attributes for one course:

- Name - should be unique
- Description
- Start Date
- End Date - can be nullable

Here is how the admin page of the `Course` should look like:

| Name                        | Description | Start Date | End Date   | Duration |
| --------------------------- | ----------- | ---------- | ---------- | -------- |
| Programming 101 with Python | Python!     | 01.01.2016 | 01.03.2016 | 3 months |
| Programming 101 with Ruby   | Ruby.       | 10.01.2016 | 01.03.2016 | 2 months |

The **Duration** should be an approximation. Figure it out ;)

## Lectures

Having only courses is pointless. So lets add some lectures to the mix!

Our lecture should have:

- Unique Identifier
- Name
- Week - like the weeks in HackBulgaria
- course - Foreign key
- URL - where the real lecture or slides are located.

## Tasks

We are interested in the following attributes for one task:

- Name - should be unique
- Description
- Due date
- Course - FK
- Lecture - optional FK

## Solutions

This is the interesting part of our system.
Our solution should have:

- Task - FK
- Date
- URL - link with solution in Github. **Validate the GitHub url and don't allow models with wrong urls to be saved!**

## Each model should have an admin page!
