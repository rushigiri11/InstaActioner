from instabot import Bot
import random
import time

# Function to perform comment action
def comment_on_post(bot, target_username, comments):
    # Get user ID of the target user
    target_user_id = bot.get_user_id_from_username(target_username)

    # Get the last media ID of the target user
    media_id = bot.get_last_user_medias(target_user_id, count=1)[0]  # Retrieve only one media post

    # Select a random comment from the list
    comment = random.choice(comments)

    # Post the comment
    bot.comment(media_id, comment)
    print(f"Commented on {target_username}'s post: {comment}")

# Function to follow a user
def follow_user(bot, target_username):
    bot.follow(target_username)
    print(f"Followed {target_username}")

# Function to like the latest post of a user
def like_latest_post(bot, target_username):
    target_user_id = bot.get_user_id_from_username(target_username)
    media_id = bot.get_last_user_medias(target_user_id, count=1)[0]  # Retrieve only one media post
    bot.like(media_id)
    print(f"Liked {target_username}'s latest post")

# Function to send a direct message to a user
def send_direct_message(bot, target_username, message):
    bot.send_message(message, [target_username])
    print(f"Sent message to {target_username}: {message}")

# Array of user credentials (username, password)
users = [
    {"username": "User_name", "password": "Password"},
    {"username": "User_name", "password": "Password"},
    # Add more users if needed
]

# Array of comments
comments = [
    "Great post!",
    "Love it!",
    "Amazing content!",
    "Keep it up!",
    "Awesome!",
    # Add more comments if needed
]

# Array of direct messages
messages = [
    "Hi there!",
    "Hello, how are you?",
    "Great profile!",
    # Add more messages if needed
]

# Target username
target_username = "rushingduck"  # Change this to the target username

# Loop through each user and perform the actions
for user in users:
    # Initialize InstaBot for the given user
    my_bot = Bot()
    my_bot.login(username=user["username"], password=user["password"], use_cookie=False)  # Disable loading saved session data

    # Perform comment action
    comment_on_post(my_bot, target_username, comments)

    # Sleep for a random duration between 30 and 60 seconds
    time.sleep(random.randint(30, 60))

    # Perform follow action
    follow_user(my_bot, target_username)

    # Sleep for a random duration between 30 and 60 seconds
    time.sleep(random.randint(30, 60))

    # Perform like action
    like_latest_post(my_bot, target_username)

    # Sleep for a random duration between 30 and 60 seconds
    time.sleep(random.randint(30, 60))

    # Perform direct message action
    message = random.choice(messages)
    send_direct_message(my_bot, target_username, message)

    # Sleep for a random duration between 30 and 60 seconds
    time.sleep(random.randint(30, 60))

    # Logout to ensure session is properly closed
    my_bot.logout()
