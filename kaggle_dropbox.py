import base64
import dropbox
import json
import os
import pickle


def get_auth(fname = '~/.kaggle/dropbox.json'):
    fname = os.path.expanduser(fname)
    with open(fname) as h:
        return json.load(h)


def save_auth(auth, fname = '~/.kaggle/dropbox.json'):
    fname = os.path.expanduser(fname)
    with open(fname, 'w') as h:
        json.dump(auth, h, indent=2)
        h.write('\n')


def auth_first_time(auth):
    auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(
        auth['key'],
        consumer_secret=auth['secret'],
        token_access_type='offline'
        )
    authorize_url = auth_flow.start()
    print("1. Go to: " + authorize_url)
    print("2. Click \"Allow\" (you might have to log in first).")
    print("3. Copy the authorization code.")
    auth_code = input("Enter the authorization code here: ").strip()
    oauth_result = auth_flow.finish(auth_code)
    return oauth_result

def refresh_token(auth):
    prev_result = auth_to_token(auth)
    dbx = dropbox.Dropbox(
            oauth2_access_token=prev_result.access_token,
            oauth2_access_token_expiration=prev_result.expires_at,
            oauth2_refresh_token=prev_result.refresh_token,
            app_key=auth['key'],
            app_secret=auth['secret']
            )
    return dbx

# ar = auth_first_time(...)
# import pickle
# auth['oauth'] = base64.b64encode(b).decode('ascii')
# kd.save_auth(auth)

def auth_to_token(auth):
    oauth = auth['oauth']
    pickled = base64.b64decode(oauth)
    return pickle.loads(pickled)

import logging
logger = logging.getLogger('kaggle_dropbox')

class KaggleDropbox:
    def __init__(self):

    def get(var_name):
        path = .... var_name
        try:
            metadata, res  = dbx.files_download('/olpa-kaggle/test.py')
        except dropbox.ApiError as e:
            logger.info("Can not get '%s': '%s'", path, e)
            if not isinstance(e, dropbox.DownloadError):
                raise e
            if not e.is_path():
                raise e
            return None
