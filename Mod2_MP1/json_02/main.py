from kivy.storage.jsonstore import JsonStore


def show_me(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'{k} = {v}')


d1 = {'dog': 1, 'cat': 2, 'mouse': 3}

print('\nPass a dictionary as keywords')
show_me(**d1)

print('\nPass Keywords')
show_me(box=4, fox=5, eggs=6)

store = JsonStore('test_1.json')
store.put('color', red=1, white=2, blue=3)
store.put('critters', **d1)
print(f"\nstore.get('critters') = {store.get('critters')}")
