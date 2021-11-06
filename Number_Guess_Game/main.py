""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : C - Number Guess Game  - main file
"""


from function import play

winning_trial = 0
losing_trial = 0
trials = 0

print(" --------- Welcome to Number Guess Game! --------- \n")

winning_trial, losing_trial, trials = play(winning_trial, losing_trial, trials)

print("You played %d game\n\tYour number of wins %d\n\tYour number of losses %d\n" % (trials, winning_trial, losing_trial))

reply = str(input("Play again!! Yes: y  No: n  "))

while reply == 'y':
    winning_trial, losing_trial, trials = play(winning_trial, losing_trial, trials)
    print("You played %d game\n\tYour number of wins %d\n\tYour number of losses %d\n" % (trials, winning_trial, losing_trial))
    reply = str(input("Play again!! Yes: y  No: n  "))

print("Thank u, see u later ...")
