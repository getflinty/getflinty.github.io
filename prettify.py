from os import listdir
from os.path import isfile, isdir, abspath, exists, join

import sys
import json

if len(sys.argv) == 1:
  sys.exit('No file or folder provided!')

destinations = map(abspath, sys.argv[1:])
json_files = []

for path in destinations:
  if not exists(path):
    print('The path %s does not exist' % path)
    continue

  if isfile(path) and path.endswith('.json'):
    json_files.append(path)
  elif isdir(path):
    destinations.extend(map(lambda x: join(path, x), listdir(path)))

for json_file_path in json_files:
  with open(json_file_path, 'r') as read_json_file:
    obj = json.load(read_json_file)
    with open(json_file_path, 'w') as write_json_file:
      json.dump(obj, write_json_file, indent=2)
  print('Prettified %s' % json_file_path)
