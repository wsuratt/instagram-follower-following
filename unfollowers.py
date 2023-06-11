import json

followers_file_path = 'followers_and_following/followers_1.json'
following_file_path = 'followers_and_following/following.json'

with open(followers_file_path) as file:
    followers_data = json.load(file)

with open(following_file_path) as file:
    following_data = json.load(file)

followers = [item['string_list_data'][0]['value'] for item in followers_data]
following = [item['string_list_data'][0]['value'] for item in following_data['relationships_following']]

unfollowers = [value for value in following if value not in followers]

print(unfollowers)


