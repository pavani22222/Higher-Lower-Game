def comp_sen(i,n,d,c):
  print(f"{data[i][n]} {data[i][d]} from {data[i][c]}")


def followers(i,fc):
  return (data[i]["follower_count"])


from game_data import data
import random

from art import logo,vs

def game():
  score=0
  win=True
  while win==True:
    i=random.randint(0,50)
    j=random.randint(0,50)
    comp_sen(i,"name","description","country")
    print(vs)
    comp_sen(j,"name","description","country")
    guess=(input("Guess who has Higher followers on insta : f1/f2 "))
    f1=followers(i,"follower_count")
    f2=followers(j,"follower_count")
    print(f"f1 has {f1}M followers")
    print(f"f2 has {f2}M followers")
    if guess=="f1" and f1>f2:
      print("You Won !")
      score+=1
      print(f"Your score is {score}")
    elif guess=="f2" and f2>f1:
      print("You Won !")
      score+=1
      print(f"Your score is {score}")
    else:
      # print(score)
      print("You Lost !")
      print(f"Your score is {score}")
      win=False

print(logo)     
game()

  

