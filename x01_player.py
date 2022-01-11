#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  x = str(input("enter: "))
  if x == "rock":
    x = 0
  if x == "paper":
    x = 1
  if x == "scissors":
    x = 2
  return x


if __name__ == "__main__":
  player = playerChoice()
  print(player)
