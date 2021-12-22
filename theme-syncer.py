import sys
import os
import config as cfg
import random

working_dir = sys.path[0]


def set_kb_rgb(theme):
    os.system(f'sudo {cfg.rgb_controller} {cfg.themes[f"theme_{theme}"]["kb_rgb"]}')


def set_wallpaper(theme):
    os.system(f'{cfg.wallpaper_controller} {cfg.themes[f"theme_{theme}"]["wallpaper"]}')


def set_apps(theme):
    for app in cfg.themes[f"theme_{theme}"]["app_themes"]:
        os.system(cfg.app_commands[app].format(cfg.themes[f"theme_{theme}"]["app_themes"][app]))


def set_theme(theme):
    set_wallpaper(theme)
    set_kb_rgb(theme)
    set_apps(theme)


def cycle_theme():
    with open(f'{working_dir}/current_theme.txt', 'r') as f:
        current = int(f.read())
        if current == len(cfg.themes):
            current = 0
        set_theme(current+1)
    with open(f'{working_dir}/current_theme.txt', 'w') as f:
        f.write(str(current+1))


def main():
    args = sys.argv[1:]
    if len(args) == 0 or args[0] == 'help':
        print('||========== THEME SYNCER ==========||\n'
              'Usage:   python theme-syncer.py <arg>\n'
              'Arguments:'
              '\n\tcycle\tSwitch to next theme'
              '\n\trandom\tSwitch to random theme'
              '\n\t<num>\tSwitch to nth theme (e.g 1)')
        sys.exit()
        
    if args[0].isdigit():
        if len(args) > 1:
            print('Error: Too many arguments'
            '\nUsage: python theme-syncer.py <arg>')
            sys.exit()
        if not 0 < int(args[0]) <= len(cfg.themes):
            print(f'Error:  Theme number out of range (1-{len(cfg.themes)})')
            sys.exit()

        set_theme(args[0])
        
    elif args[0] == 'cycle':
        cycle_theme()
        
    elif args[0] == 'random':
        set_theme(random.randint(1, len(cfg.themes)))

    
if __name__ == '__main__':
    main()
