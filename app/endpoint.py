from flask import request, render_template_string, render_template

from app import app, chatwork
from app.constants import *
from app.helpers import get_room_id

@app.route('/', methods=['POST'])
def handle_payload():
    if request.headers.has_key('X-Github-Event'):
        event_type = request.headers['X-Github-Event']
        payload = request.json
        repo = payload['repository']['full_name']
        params = dict(repo=repo)
        room_id = get_room_id(repo)

        if event_type == EVENT_COMMIT_COMMENT:
            params['body'] = payload['comment']['body']
            params['url'] = payload['comment']['html_url']
            params['author'] = payload['comment']['user']['login']

            message = render_template(event_type, **params)
            chatwork.get_room(room_id).post_message(message)

        if event_type == EVENT_PING:
            return 'pong'

    return 'OK'
