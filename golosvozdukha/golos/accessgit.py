import json
import base64

from github3 import login

#-----------------------------------------

username = 'strigidaeinsomnie'
password = 'inrpdlf13'
repositoryname = 'inproduction'

#------------------------------------------

gh = login(username, password)
repo = gh.repository(username, repositoryname)
branch = repo.branch("master")

tree = branch.commit.commit.tree.recurse()
filename = tree.tree[6]

blob = repo.blob(filename._json_data['sha'])

config_json = blob.content
config        = json.loads(base64.b64decode(config_json))
text = config.decode('utf-8')
print(text)
