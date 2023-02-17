import json

# Load the data from the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# Print the header
print("Interface Status")
print("=" * 100)
print("DN                                                 Description           Speed    MTU  ")
print("-" * 100)

# Print the interface information
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    desc = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print(f"{dn:<50} {desc:<20} {speed:>7} {mtu:>6}")
