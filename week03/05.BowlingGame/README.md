## Bowling Game

### Game Basics

One game of bowling consists of 10 frames. The minimum score for a game is 0 and a maximum is 300.
Each frame consists of two chances to knock down ten pins. In the bowling game we use "pins", instead of "points".

- Strikes -
  Knocking down all 10 pins on your first ball is called a strike, denoted by an "X" on the score sheet. A strike is worth 10, plus the value of your next 2 rolls.
  At minimum, your score for a frame in which you throw a strike will be 10 (10+0+0).
  At best, your next two shots will be strikes, and the frame will be worth 30 (10+10+10).
  Say you throw a strike in the first frame. Technically, you don't have a score yet.
  You need to throw two more balls to figure out your total score for the frame.
  In the second frame, you throw a 6 on your first ball and a 2 on your second ball. Your score for the first frame will be 18 (10+6+2).
- Spares -
  If it takes two shots to knock down all ten pins, it's called a spare, denoted by "N /". A spare is worth 10, plus the value of your next roll.
  Say you throw a spare in your first frame. Then, in your first ball of the second frame, you throw a 7.
  Your score for the first frame will be 17 (10+7).
  The maximum score for a frame in which you get a spare is 20 (a spare followed by a strike), and the minimum is 10.
- Open Frames -
  If, after 2 shots, at least 1 pin is still standing, it's called an open frame. If you don't get a strike or a spare in a frame, your score is the total number of pins you knock down. If you knock down 3 pins on your first ball and 2 on your second, your score for that frame is 5.
- The Tenth Frame -
  In the sample score, three shots were thrown in the tenth frame. This is because of the bonuses awarded for strikes and spares. If you throw a strike on your first ball in the tenth frame, you need two more shots to determine the total value of the strike. If you throw a spare on your first two balls in the tenth frame, you need one more shot to determine the total value of the spare. This is called a fill ball.
  If you throw an open frame in the tenth frame, you won't get a third shot. The only reason the third shot exists is to determine the full value of a strike or spare.
  **Use OOP and follow the TDD to implement the Bowling game**
- Help -
  You can use this [calculator](https://www.bowlinggenius.com/) to understand the rules better.

```python3.6
game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
game.result # 65
game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
game.result # 0
game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
game.result # 300
game = BowlingGame([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])
game.result # invalid number of frames
```
