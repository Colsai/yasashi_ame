import os
import curses

HEALTH_MAX = 100

def draw_bar(label, value, max_value, length=20):
    filled = int(length * value / max_value)
    empty = length - filled
    bar = '█' * filled + ' ' * empty
    return f"{label}: [{bar}] {value}/{max_value}"


def display_scene_gui(scene_path, health, location, clear=True, wait=True):
    """Display a scene using a simple curses-based GUI."""

    def _draw(stdscr):
        curses.curs_set(0)
        if clear:
            stdscr.clear()
        height, width = stdscr.getmaxyx()

        sidebar_width = 30
        main_width = width - sidebar_width

        main_win = curses.newwin(height, main_width, 0, 0)
        side_win = curses.newwin(height, sidebar_width, 0, main_width)

        with open(scene_path, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]

        # Render main window content
        main_win.box()
        for idx, line in enumerate(lines):
            if idx >= height - 2:
                break
            trimmed = line[:main_width - 2]
            main_win.addstr(1 + idx, 1, trimmed)

        # Render sidebar
        side_win.box()
        side_win.addstr(1, 2, f"Location: {location}")

        bar_length = sidebar_width - 4
        filled = int((health / HEALTH_MAX) * (bar_length - 2))
        health_bar = '█' * filled + ' ' * ((bar_length - 2) - filled)
        side_win.addstr(3, 2, "Health:")
        side_win.addstr(4, 3, '[' + health_bar + ']')
        side_win.addstr(5, 3, f"{health}/{HEALTH_MAX}")

        main_win.refresh()
        side_win.refresh()
        if wait:
            stdscr.getch()

    curses.wrapper(_draw)

def display_scene(scene_path, health, location, clear=True):
    if clear:
        os.system('clear')
    print(draw_bar('Health', health, HEALTH_MAX))
    print(f"Location: {location}")
    print('=' * 40)
    with open(scene_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.rstrip('\n'))

if __name__ == '__main__':
    health = 80
    location = 'Dreamscape'
    display_scene_gui('scenes/prologue.txt', health, location)
