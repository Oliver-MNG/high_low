from data import data
import random



def high_low(first,second,user_choise):
    score = 0
    if user_choise == first and first > second:
        return score+1
    elif user_choise == second and second > first:
        return score+1
    else:
        return 0
first = data[random.randint(0,50)]['follower_count']
second = data[random.randint(0,50)]['follower_count']

score = 0
game_end = False
while not game_end:
    second = data[random.randint(0,50)]['follower_count']

    first_person_name = [d['name'] for d in data if d['follower_count'] == first]
    first_person_description = [d['description'] for d in data if d['follower_count'] == first]
    first_person_country = [d['country'] for d in data if d['follower_count'] == first]

    second_person_name = [d['name'] for d in data if d['follower_count'] == second]
    second_person_description = [d['description'] for d in data if d['follower_count'] == second]
    second_person_country = [d['country'] for d in data if d['follower_count'] == second]

    print(f"Compare A: {first_person_name}, a {first_person_description}, from {first_person_country}.")
    print("VS")
    print(f"With B: {second_person_name}, a {second_person_description}, from {second_person_country}.")
    user_choise = input('Which has more followers? A or B: ')
    if user_choise == 'A':
        user_choise = first
    else:
        user_choise = second
    if high_low(first, second, user_choise) == 1:
        first = second
        second = data[random.randint(0,50)]['follower_count']
        score += 1
    else:
        print(f'You were wrong this time. Your score is {score}')
        game_end = True


