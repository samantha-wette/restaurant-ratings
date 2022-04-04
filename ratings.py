"""Restaurant rating lister."""

def read_ratings(file_name):
    content = open(file_name)
    restaurant_information = {}
    ratings = []
    for line in content:
        line = line.rstrip()
        ratings.append(line.split(":"))
    content.close()      

    for rating in ratings:
        name = rating[0]
        score = rating[1]
        restaurant_information[name] = score
    
    for name, score in sorted(restaurant_information.items()):
        print(f"{name} is rated at {score}.")


read_ratings('scores.txt')
