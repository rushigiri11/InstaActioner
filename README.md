# InstaActioner

InstaActioner is an advanced tool designed to automate various interactions on Instagram, helping users enhance their engagement effortlessly. It supports actions such as commenting, following, liking posts, and sending direct messages, all while allowing you to manage multiple Instagram accounts.

## Features

- **Automated Commenting**: Post random comments on the latest posts of a target user.
- **Auto-Follow**: Follow a target user automatically.
- **Post Liking**: Like the latest posts of a target user.
- **Direct Messaging**: Send random direct messages to a target user.
- **Multiple Account Support**: Manage and perform actions using multiple Instagram accounts.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rushigiri1/InstaActioner.git
    ```
2. Change to the project directory:
    ```bash
    cd InstaActioner
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Add your Instagram credentials and the target username in the script:
    ```python
    users = [
        {"username": "Add_User_Name_Here", "password": "Add_Password_Here"},
        {"username": "Add_User_Name_Here", "password": "Add_Password_Here"},
        # Add more users if needed
    ]
    
    target_username = "rushingduck"  # Change this to the target username
    ```
2. Run the script:
    ```bash
    python insta_actioner.py
    ```

## Script Breakdown

- **comment_on_post**: Posts a random comment on the latest post of the target user.
- **follow_user**: Follows the target user.
- **like_latest_post**: Likes the latest post of the target user.
- **send_direct_message**: Sends a random direct message to the target user.
- **Multiple Account Management**: Allows actions to be performed using multiple Instagram accounts, each with its own credentials.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.


## Disclaimer

This project is intended for educational purposes only. Use it responsibly and in accordance with Instagram's terms of service.
