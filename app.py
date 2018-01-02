import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '386195912:AAFy6E1I8gU--G9mTtezl_td646GFRuq-gs'
WEBHOOK_URL = 'https://33e60252.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
#--------------------
machine = TocMachine(
    states=[
        'user',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
        'work',
        'free'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'monday',
            'conditions': 'is_going_to_monday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'tuesday',
            'conditions': 'is_going_to_tuesday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'wednesday',
            'conditions': 'is_going_to_wednesday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thursday',
            'conditions': 'is_going_to_thursday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'friday',
            'conditions': 'is_going_to_friday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'saturday',
            'conditions': 'is_going_to_saturday'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'sunday',
            'conditions': 'is_going_to_sunday'
        },
        {
            'trigger': 'advance',
            'source':  [
                'monday',
                'tuesday',
                'wednesday',
                'thursday',
                'friday',
                'saturday',
                'sunday'
            ],
            'dest': 'work',
            'conditions': 'is_going_to_work'
        },
        {
            'trigger': 'advance',
            'source':  [
                'monday',
                'tuesday',
                'wednesday',
                'thursday',
                'friday',
                'saturday',
                'sunday'
            ],
            'dest': 'free',
            'conditions': 'is_going_to_free'
        },
        {
            'trigger': 'go_back',
            'source': [
                'work',
                'free'
            ],
            'dest': 'user'
        }
    ],
    
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

#--------------------
def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
