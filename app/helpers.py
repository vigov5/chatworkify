from app import app

def get_room_id(repo):
    if app.config['REPO_ROOM_IDS'].has_key(repo):
        return app.config['REPO_ROOM_IDS'][repo]
    else:
        return app.config['DEFAULT_ROOM_ID']
