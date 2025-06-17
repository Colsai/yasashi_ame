import os

HEALTH_MAX = 100

def draw_bar(label, value, max_value, length=20):
    filled = int(length * value / max_value)
    empty = length - filled
    bar = '█' * filled + ' ' * empty
    return f"{label}: [{bar}] {value}/{max_value}"


def display_scene(scene_path, health, location, clear=True):
    if clear:
        os.system('clear')
    print(draw_bar('Health', health, HEALTH_MAX))
    print(f"Location: {location}")
    print('=' * 40)
    with open(scene_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.rstrip('\n'))
