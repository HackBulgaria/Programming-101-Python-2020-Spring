# Belote Declarations

[Belote](https://en.wikipedia.org/wiki/Belote) is one of the most famous card games in Bulgaria. Your task is to implement just part of it - the possible declarations (announcements) in the first trick.

## Explanations

> TL;DR: If you are familiar with the game of Belote this paragraph may be skipped.

The Belote game is explained well in the above link from Wikipedia. There are a lot of rules but most of them do not apply for the declarations which are our target for this task. Here, I will try to summarize the rules:

- The game is played with all 4 ranks `(Clubs, Diamonds, Hearts, Spades)` and the suites from 7 to A `(7, 8, 9, 10, J, Q, K, A)`.
- The game is played by 2 teams -> Team X = Player 1 + Player 3; Team Y = Player 2 + Player 4
- Each player has 8 cards
- The announcements are made in consecutive order by the players.

### Belote

- A player can announce "belote" if he has a K and Q from the same rank.
- You can have a "belote" only from the rank that is the same with the game that is played (Ks + Qs is a belote only in a game of Spades)
- In a game of "All trumps" -> you can have belote from all of the ranks
- In a game of "No trumps" -> **there are no belotes**

### Consecutive cards

- A player can announce "tierce" (20 points) if he has 3 consecutive cards from the same rank ( e.g. 7c, 8c, 9c ).
- A player can announce "quarte" (50 points) if he has 4 consecutive cards from the same rank ( e.g. 10h, Jh, Qh, Kh ).
- A player can announce "quinte" (100 points) if he has 5 (or more) consecutive cards from the same rank ( e.g. 8s, 9s, 10s, Js, Qs ).
- In a game of "No trumps" -> **there are no tierces, quartes or quintes**

### Carre

- A player can announce "carre" if he has 4 cards with the same suite ( e.g. Js, Jh, Jd, Jc ).
- **4 7's or 4 8's are not considered carre**
- In a game of "No trumps" -> **there are no carres**
- Pointing:
  - carre of 10, Q, K, A = 100 points
  - carre of 9's = 150 points
  - carre of J's = 200 points
- **NOTE: One card cannot be part from a carre and tierce/quarte/quinte in the same time. It can be part of a belote though.**. Let's say you have the following cards: `['7s', '8s', '9s', '9c', '9d', '9h', 'Kc', 'As']`. In this case the program is expected to output carre of 9's. You can still announce only tierce, but it gives you less points.

## Scoring

The game is won by the team who first make > 150 points (If you have 150 points, the game is not over!)

For this task, the points of one team will be calculated by summing their points from their announces.

There are multiple rules connected to the priority of the announces. They apply only to between the teams:

- The general rule: tierce < quarte < quinte. This means that if Team 1 has tierce and Teams 2 has quinte, the tierce of Team 1 should be excluded from the points.
- If two enemy players have same sequences (e.g. player 1 and player 2 both have tierce) the one that is to a higher rank wins. If the sequences are equal, both of them should be excluded.
- All belotes hold good!
- All carres hold good!

### Example rounds

```
Team 1: 7s 8s 9s - tierce
Team 2: 7c 8c 9c 10c - quarte

Result: Team 1 has no tierce, because it's killed by the quarte of the other team => 0 points. Team 2 has quarte => 50 points
```

```
Team 1: Jd Qd Kd - tierce and belote
Team 2: 7c 8c 9c - tierce

Result: Team 1 has no tierce and belote => 40 points. Team 2 has no tierce, because it's lower than the tierce of the other team => 0 points

*NOTE: Rules for the belotes and the current played game should be applied*
```

```
Team 1: Jd Qd Kd - tierce and belote
Team 2: Js Qs Ks - tierce and belote

Result: Team 1 has only belote, the tierce is killed as it's equal to the tierce of the other team  => 20 points. Team 2 has only belote, the tierce is killed as it's equal to the tierce of the other team  => 20 points.

*NOTE: Rules for the belotes and the current played game should be applied*
```

```
Team 1: 10s 10d 10h 10c - carre of 10's
Team 2: 9s 9d 9h 9c - carre of 9's

Result: Team 1 has carre of 10's => 100 points. Team 2 has care of 9's => 150 points
```

```
Team 1: 10s 10d 10h 10c - carre of 10's
Team 2: 7s 8s 9s - tierce

Result: Team 1 has carre of 10's => 100 points. Team 2 has tierce => 20 points
```

```
Team 1: 7s 8s 9s + 9d 10d Jd - 2 tierces
Team 2: 7h 8h 9h - tierce

Result: Team 1 has 2 tierces => 40 points. Team 2 has no tierce, becase one of the tierces of the other team is higher => 0 points
```

```
Team 1: 7s 8s 9s + 9d 10d Jd Qd - tierce & quarte
Team 2: 9c 10c Jc Qc - quarte

Result: Team 1 has nothing because the quartes are equal and the quarte of the other team kills the tierce => 0 points. Team 2 has no quarte, because the quartes are equal => 0 points
```

## The task

You should imitate a game of Belote where the scores are generated only from the declarations of the players.

Team and player names should inputted from the user.
Example:

```
python3 belote.py

Team 1 name: Mecheta
Team 2 name: Koteta

"Mecheta" players: Marto, Rado
"Koteta" players: Gosho, Pesho
```

The two teams should alternate when declaring. When the program is started, the first player is player 1 from team 1 ('Marto'). In other words, the order of the players after the above input is: 'Marto' -> 'Gosho' -> 'Rado' -> 'Pesho'.
After each round, the first player from the last round becomes last: 'Gosho' -> 'Rado' -> 'Pesho' -> 'Marto'.
When a game is won by a team, a random player from this team starts the first round of the next game.

The points from one round are calculated by summing the points from the declarations of each team. For example, if 'Marto' has tierce (20) and 'Rado' has quarte (50), their result from the round is 70 points.
**NOTE: In the real game of Belote, these points are divided by 10. Don't do this for this task!!!**

The program should finish when one of the teams win 2 games.

One game is won by the first team that scores more than 150 points. If both of the teams have more than 150 points, the game is won by the team who has more points. If the points are equal, the game should continue until one of the teams shoot ahead.

After each round, the points from the current round should be written into the `results.txt` file.
In the following example we will see the expected format of the file:

```
     Mecheta     |     Koteta
=================================
20               | 100
20 + 50          | 100 + 0
```

This is how you should mark when a game is won by a team:

```
     Mecheta     |     Koteta
=================================
20               | 100
20 + 20          | 100 + 20
40 + 50          | 120 + 0
90 + 100         | 120 + 50
190              | 170
=================================
       (1)       |      (0)
=================================
```

After each round, the cards and the announcements of each player should be written in `data.json` file.
Let's say we have this round:

```
Marto: ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"]  # team Mecheta
Gosho: ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"]  # team Koteta
Rado: ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"]  # team Mecheta
Pesho: ["7h", "8h", "9h", "10h", "Jc", "Qh", "Ks", "Ah"]  # team Koteta
```

```json
{
  "game 1": {
    "round 1": {
      "contract": "Hearts",
      "Mecheta": {
        "Marto": {
          "cards:": ["7s", "8s", "9s", "10c", "Jd", "Qh", "Kh", "As"],
          "announcements": ["belote"],
          "points": 20
        },
        "Rado": {
          "cards:": ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"],
          "announcements": [],
          "points": 0
        }
      },
      "Koteta": {
        "Gosho": {
          "cards:": ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"],
          "announcements": [],
          "points": 0
        },
        "Pesho": {
          "cards:": ["7h", "8h", "9h", "10h", "Jc", "Qd", "Ks", "Ah"],
          "announcements": ["quarte"],
          "points": 50
        }
      }
    }
    // rest of the rounds here ....
  }
}
```
