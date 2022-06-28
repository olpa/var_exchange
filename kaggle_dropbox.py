import base64
import dropbox
import json
import logging
import os
import pickle

DEFAULT_AUTH_FILE = '~/.kaggle/dropbox.json'
logger = logging.getLogger('kaggle_dropbox')


def get_auth(fname):
    fname = os.path.expanduser(fname)
    with open(fname) as h:
        auth = json.load(h)
    for required in ('key', 'secret', 'oautjhh'):
        assert required in auth, f"Auth json should have '{required}' key"
    return auth


def save_auth(auth):
    fname = os.path.expanduser(fname)
    with open(fname, 'w') as h:
        json.dump(auth, h, indent=2)
        h.write('\n')


def auth_first_time():
    key = input('Enter the application key:').strip()
    secret = input('Enter the application secret:').strip()
    auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(
        key,
        consumer_secret=secret,
        token_access_type='offline'
        )
    authorize_url = auth_flow.start()
    print("1. Go to: " + authorize_url)
    print("2. Click \"Allow\" (you might have to log in first).")
    print("3. Copy the authorization code.")
    auth_code = input("Enter the authorization code here: ").strip()
    oauth = auth_flow.finish(auth_code)
    s_oauth = pickle.dump(oauth)
    s_oauth = base64.base64encode(s_oauth)
    print('Put the following json to {DEFAULT_AUTH_FILE} or TODO:\n', {
        'key': key,
        'oauth': s_oauth,
        'secret': secret,
        })

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

def extract_oauth_object(auth):
    oauth = auth['oauth']
    pickled = base64.b64decode(oauth)
    return pickle.loads(pickled)

class KaggleDropbox:
    def __init__(self,
            auth_file=DEFAULT_AUTH_FILE,
            namespace='',
            **dropbox_options):
        self.namespace = namespace
        auth = get_auth(auth_file)
        oauth = extract_oauth_object(auth)
        assert isinstance(oauth, string)  # FIXME
        self.dbx = dropbox.Dropbox(
                oauth2_access_token=oauth.access_token,
                oauth2_access_token_expiration=oauth.expires_at,
                oauth2_refresh_token=oauthj.refresh_token,
                app_key=auth['key'],
                app_secret=auth['secret']
                )

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


