import json
import sys
import time

output = dict()
output['testing'] = dict()
output['testing']['one'] = 'two'

index = 0

for i in sys.argv:
    output[index] = i
    index = index + 1

count = 100
while index < count:
    print(f'Adding some data {index}')
    index += 1
    time.sleep(1)

print(json.dumps(output))

sys.exit(0)
