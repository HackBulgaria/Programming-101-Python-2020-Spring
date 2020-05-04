# Hack Bulgaria Cinema Reservation System

We are going to the cinema! But the reservation systems are down and the cinema officials don't let people enter without reservations. So we offered to make them a new reservation system that will allow us to go and watch the newest movies.

## Problem 0 - The database

No complex stuff here. Just a few simple tables:

### Movies

| id  | name                            | rating |
| --- | :------------------------------ | :----: |
| 1   | The Hunger Games: Catching Fire |  7.9   |
| 2   | Wreck-It Ralph                  |  7.8   |
| 3   | Her                             |  8.3   |

### Projections

| id  | movie_id | type |    date    | time  |
| --- | -------- | :--: | :--------: | :---: |
| 1   | 1        |  3D  | 2020-04-01 | 19:10 |
| 2   | 1        |  2D  | 2020-04-01 | 19:00 |
| 3   | 1        | 4DX  | 2020-04-02 | 21:00 |
| 4   | 3        |  2D  | 2020-04-05 | 20:20 |
| 5   | 2        |  3D  | 2020-04-02 | 22:00 |
| 6   | 2        |  2D  | 2020-04-02 | 19:30 |

### Users

| id  | username          |   password   |
| --- | ----------------- | :----------: |
| 1   | Martin Angelov    | **\*\*\*\*** |
| 2   | Ivo Donchev       | **\*\*\*\*** |
| 3   | Radoslav Georgiev | **\*\*\*\*** |
| 4   | Rositza Zlateva   | **\*\*\*\*** |

Passwords should be with length **at least 8 symbols, 1 capital letter and a special symbol**. Also, don't forget to **hash** the passwords!

### Reservations

| id  | user_id | projection_id | row | col |
| --- | ------- | ------------- | :-: | :-: |
| 1   | 3       | 1             |  2  |  1  |
| 2   | 3       | 1             |  3  |  5  |
| 3   | 3       | 1             |  7  |  8  |
| 4   | 2       | 3             |  1  |  1  |
| 5   | 2       | 3             |  1  |  2  |
| 6   | 5       | 5             |  2  |  3  |
| 7   | 6       | 5             |  2  |  4  |

### Things to note

- For each projection we assume the hall to be a 10x10 matrix.
- All data presented here is just an example. If you want, you can make up your own data. For example, implement a ticketing system after you have the reservations in place.

## Problem 1 - The CLI (Command-Line Interface)

Our cinema reservation system will be very simple. We will use the console for user interactions:

- `show movies` - print all movies ORDERed BY rating
- `show movie projections <movie_id> [<date>]` - print all projections of a given movie for the given date (date is optional).

  1. ORDER the results BY date
  2. For each projection, show the total number of spots available.

- `make reservation` - It's showtime!

  1. Check if user is logged
  2. If not, first action is to log the user into the system.
  3. If already logged, the user can make a reservation
  4. Make him choose how many seats he want to reserve
  5. Call `show movies` and make the user choose a movie by id
  6. Call `show movie projections` for the chosen `<movie_id>` and make the user choose a projection

  - _If the available spots for a projection are less than the number of reservations needed, print an appropriate message and stay at step 6_;

  7. Show all available seats
  8. Make the user choose his seats - validate the input
  9. Format the reservation appropriately and show it to the user
  10. On `finalize`, save all the info and wish a happy cinema!
  11. **At each step, allow for `cancel` option.**

- On `cancel reservation <name>` - disintegrate given person's reservation (**NOTE**: reservations cannot be so easily removed)
- On `exit` - close Pandora's Box before it's too late.
- On `help` - show a list of valid options

### Things to note

- Reuse code and write tests
- Try not to build everything in one place.
- Make use of the following techniques : **OOP, TDD, SQL, MVC**.

## Problem 2 - Decorators

We want you to implement a decorator for atomic transactions on each of the query you execute with the cinema application!

```python
@atomic
def show_movies():
    pass
```

We want to make sure the user is logged in in order to use the system.

```python
@login_required
def show_movies():
    pass
```

Log each reservation in the system in a file.

```python

@log_info
def finalize():
    pass
```

## Examples

### Show movies

```
> show movies
Current movies:
[1] - The Hunger Games: Catching Fire (7.9)
[2] - Wreck-It Ralph (7.8)
[3] - Her (8.3)
```

### Show movie projections

```
> show movie projections 2
Projections for movie 'Wreck-It Ralph':
[5] - 2020-04-02 19:30 (2D)
[6] - 2020-04-02 22:00 (3D)
> show movie projections 1 2020-04-01
Projections for movie 'The Hunger Games: Catching Fire' on date 2020-04-01:
[1] - 19:00 (3D)
[2] - 19:10 (2D)
```

### Make a reservation

```
> make reservation
You need to a user in the system to make reservations!
Username: Rositsa Zlateva
Password:
Hello, Rositsa Zlateva
............
```

### Make a reservation

```
> make reservation
Hello, Rositsa Zlateva
Step 1 (User): Choose number of tickets> 2
Current movies:
[1] - The Hunger Games: Catching Fire (7.9)
[2] - Wreck-It Ralph (7.8)
[3] - Her (8.3)
Step 2 (Movie): Choose a movie> 2
Projections for movie 'Wreck-It Ralph':
[5] - 2020-04-02 19:30 (2D) - 98 spots available
[6] - 2020-04-02 22:00 (3D) - 100 spots availabe
Step 3 (Projection): Choose a projection> 5
Available seats (marked with a dot):
   1 2 3 4 5 6 7 8 9 10
1  . . . . . . . . . .
2  . . X X . . . . . .
3  . . . . . . . . . .
4  . . . . . . . . . .
5  . . . . . . . . . .
6  . . . . . . . . . .
7  . . . . . . . . . .
8  . . . . . . . . . .
9  . . . . . . . . . .
10 . . . . . . . . . .
Step 4 (Seats): Choose seat 1> (2,3)
This seat is already taken!
Step 4 (Seats): Choose seat 1> (15, 16)
Lol...NO!
Step 4 (Seats): Choose seat 1> (7,8)
Step 4 (Seats): Choose seat 2> (7,7)
This is your reservation:
Movie: Wreck-It Ralph (7.8)
Date and Time: 2020-04-02 19:30 (2D)
Seats: (7,7), (7.8)
Step 5 (Confirm - type 'finalize') > finalize
Thanks.
```

## DISCLAIMER

Customize it! Think of some add-ons and extras and add it to the task!
