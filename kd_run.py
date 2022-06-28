import argparse
import dropbox
import os
import sys

import kaggle_dropbox as kd

def parse_command_line():
    parser = argparse.ArgumentParser(description = 'Exchange Python variables through Dropbox')
    parser.add_argument('--basedir', type=str, help='parent directory on Dropbox')
    parser.add_argument('--get-file', type=str)
    parser.add_argument('--put-file', type=str)
    parser.add_argument('--get-var', type=str, help='get file from dropbox and print as python variable')
    args = parser.parse_args()
    assert bool(args.get_file) + bool(args.put_file) + bool(args.get_var) == 1, "One and only one of the arguments '--get-file', '--put-file' and '--get-var' is expected, got:" + str(args)
    return args

#auth = kd.get_auth()
# print(auth)
# kd.save_auth(auth)
#token = kd.auth_to_token(auth)
# print(dir(token))

# refresh token:
# https://github.com/dropbox/dropbox-sdk-python/blob/main/example/oauth/commandline-oauth-scopes.py
# https://github.com/dropbox/dropbox-sdk-python/blob/main/example/oauth/commandline-oauth-scopes.py#L79


#DROPBOX_ACCESS_TOKEN = token.access_token

#dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
#print(dbx)
# print(dir(dbx))
#print(dbx.files_list_folder('/olpa-kaggle'))
#print(dbx.files_list_folder('/'))
#print(dbx.files_list_folder('olpa-kaggle'))
#print(dbx.files_list_folder('kaggle'))
#print(dbx.files_list_folder('', recursive=True))

def make_dbx_name(fname):
    return f'/olpa-kaggle/{os.path.basename(fname)}-py'

def upload_file(fname):
    with open(fname, 'rb') as h:
        dbx.files_upload(h.read(), make_dbx_name(fname))

def download_file(fname):
    dbx_name = make_dbx_name(fname)
    print('Download:', dbx_name, '->', fname + '.dbx')
    metadata, res  = dbx.files_download(dbx_name)
    print('meta:', metadata)
    print('res:', res)
    print('res.content:', res.content)
    with open(fname + '.dbx', 'wb') as h:
        h.write(res.content)


# upload_file('test.py')
# download_file('test.py')

def main():
    args = parse_command_line()
    print(args)

main()
