
import json
r = open('whitelist.json').read()
r = json.loads(r)
#print(r.keys())
print('''[SwitchyOmega Conditions]
@with result
''')
for k, v in sorted(r.items()):
    for value in sorted(v.keys()):
        print("*."+value+"."+k+" +direct")

print()
print('* +alihk-ss-0')