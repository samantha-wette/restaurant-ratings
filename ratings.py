"""Restaurant rating lister."""

def read_ratings(file_name):
    content = open(file_name)
    restaurant_information = {}
    # ratings = []
    for line in content:
        line = line.rstrip()
        line = line.split(":")
        # print(f"=================={line}")        
        # print(restaurant_information)
        # ratings.append(line.split(":"))
        restaurant_information[line[0]] = int(line[1]) 

           
    content.close()      

    added_restaurant = input('What restaurant would you like to rate? ')
    added_rating = input('How would you rate that restaurant from 1 to 5? ')
    restaurant_information[added_restaurant] = int(added_rating)

    #ratings.append([added_restaurant, added_rating])

    # for rating in ratings:
    #     name = rating[0]
    #     score = rating[1]
    #     restaurant_information[name] = score
    
    for name, score in sorted(restaurant_information.items()):
        print(f"{name} is rated at {score}.")

    

read_ratings('scores.txt')
