import logging
from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager, HassRemote
import homeassistant.remote as remote

app = Flask(__name__)
assist = Assistant(app)
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
hass = HassRemote('YOUR Home Assistant PASSWORD')


@assist.action('greeting')
def greet_and_start():
    speech = "Hey! Are you male or female?"
    return ask(speech)


@assist.action("user-gives-gender")
def ask_for_color(gender):
    if gender == 'male':
        gender_msg = 'Sup bro!'

    else:
        gender_msg = 'Haay gurl!'

    speech = gender_msg + ' What is your favorite color?'
    return ask(speech)


@assist.action('give-color', mapping={'color': 'sys.color'})
def repeat_color(color):
    speech = 'Ok, {} is an okay color I guess.'.format(color)
    return ask(speech)


if __name__ == '__main__':
    app.run(debug=True)
