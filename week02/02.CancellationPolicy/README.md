# Cancellation Policy

You are a co-working space and you have many floors, rooms and desks.
Your customers can book rooms and desks for their needs.
If a customer decides to cancel his or her booking just before it starts we may need to fee him.

The cancellation policy conditions are in the given format:

```
[
  { hours: 24, percent: 10 },
  { hours: 12, percent: 50 },
  { hours: 6, percent: 80 },
  { percent: 100 }
]
```

The above example means: You will be feed with:

- 10% if you cancel your booking more than 24 hours before it starts
- 50% if you cancel it for less or equal than 24 hours and more than 12 hours before it starts
- 80% if you cancel it for less or equal than 12 hours and more than 6 hours before it starts
- 100% if you cancel it for less or equal than 6 hours before it starts.

Notes:

- Make sure the cancellation policy is sorted
- Only the dictionary that has no `hours` key is required
- The max `hours` value is 24

Using TDD, implement a program that calculates the price that a customer needs to pay if he/she wants to cancel his/her booking **now**.
