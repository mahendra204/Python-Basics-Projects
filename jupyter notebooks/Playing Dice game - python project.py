
import random as rn
def roll():
  min_val=1
  max_val=6
  return rn.randint(min_val,max_val)
while True:
  players=int(input('enter the number of players:'))
  if (1<players<10):
    print(players)
    break
  else:
    print('players must be greater than 1')
max_score=20
players_score=[0 for i in range(players)]
while max(players_score)<max_score:
  for j in range(players):
    print('player:',j+1,'turn has started now')
    cur_score=0
    while True:
      player_turn=input('do you want to play?(y/n):')
      if player_turn=='y':
        value=roll()
      else:
        break
      if value==1:
        print('you rolled 1. Turn over')
        break
      else:
        print('you rolled:',value)
        cur_score+=value
      print('your cur_score is:', cur_score)
    players_score[j]+=cur_score
    print('your total score is:', players_score[j])
max_value=max(players_score)
winning_player_idx=players_score.index(max_value)
print('player number:', winning_player_idx+1, 'is the winner with a score of', max_value)





