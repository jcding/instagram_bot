# Instagram Bot

Too lazy to go on Instagram to engage with others? Too busy to grow your Instagram account by yourself? Don't worry, the Instagram Bot has got your back! It will like people's posts for you. It uses training data and Chatterbot to automatically respond to comments 😲😲

## Getting Started

```
git clone https://github.com/jcding/instagram_bot.git
```

### Prerequisites

Requires:
* Python 3

### Required Packages
* Selenium
* ChatterBot

### Installing

All you need to do is:

```
cd instagram_bot
source bin/activate
pip install -e .

# Install Instagram API tool used for comment scraping
pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0
pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0 --upgrade
```

### Running
Running Instagram Bot:
```
python3 main.py
```

Training the Commenting AI:
```
cd instagrambot/comment_bot

# Training the AI
python3 bot_training.py

# Conversate with the AI through the command line
python3 conversate.py
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Jason Ding** - *Initial work* - [jcding](https://github.com/jcding)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to [ping](https://github.com/ping) for his Instagram API: (https://github.com/ping/instagram_private_api)
