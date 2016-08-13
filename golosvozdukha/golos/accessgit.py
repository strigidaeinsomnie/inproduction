import json
import base64

from github3 import login

#-----------------------------------------

username = 'strigidaeinsomnie'
password = 'inrpdlf13'
repositoryname = 'poeziya'

#------------------------------------------

gh = login(username, password)
repo = gh.repository(username, repositoryname)
branch = repo.branch("master")

tree = branch.commit.commit.tree.recurse()
print(len(tree.tree))

filename = tree.tree[1]
print(filename.path)

blob = repo.blob(filename._json_data['sha'])

config_json = blob.content
config = base64.b64decode(config_json)
text = config.decode('utf-8')
print(text)
