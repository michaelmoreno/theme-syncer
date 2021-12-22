# Program to change keyboard backlight color

import os

rgb_controller = '~/rogauracore/rogauracore'
# Program to change wallpaper
wallpaper_controller = 'feh --bg-scale'

wallpaper_path = '~/Pictures/wallpapers'

app_commands = {
    'vscode': 'tmp=$(mktemp) && theme="{}" && jq --arg a "$theme" \'."workbench.colorTheme" = $a\' ~/.config/Code/User/settings.json > "$tmp" && mv "$tmp" ~/.config/Code/User/settings.json'
}


themes = {
    'theme_1': {
        'wallpaper': f'{wallpaper_path}/bluedear.jpg',
        'kb_rgb': 'cyan',
        'app_themes': {
            'vscode': 'Atom One Dark',
        }
    },
    'theme_2': {
        'wallpaper': f'{wallpaper_path}/redmountains.jpg',
        'kb_rgb': 'red',
        'app_themes': {
            'vscode': 'Monokoi Pro',
        }   
    },
    'theme_3': {
        'wallpaper': f'{wallpaper_path}/green1.jpg',
        'kb_rgb': 'green',
        'app_themes': {
            'vscode': 'Monokai Pro (Filter Machine)',
        }
    },
    'theme_4': {
        'wallpaper': f'{wallpaper_path}/purpleplanets.jpg',
        'kb_rgb': 'magenta',
        'app_themes': {
            'vscode': 'Palenight (Mild Contrast)',
        }
    },
    'theme_5': {
        'wallpaper': f'{wallpaper_path}/orangeblossom.jpg',
        'kb_rgb': 'red',
        'app_themes': {
            'vscode': 'Monokai Pro',
        }
    },
    'theme_6': {
        'wallpaper': f'{wallpaper_path}/pinktree.jpg',
        'kb_rgb': 'magenta',
        'app_themes': {
            'vscode': 'Palenight (Mild Contrast)',
        }
    },
    'theme_7': {
        'wallpaper': f'{wallpaper_path}/redblossom.jpg',
        'kb_rgb': 'red',
        'app_themes': {
            'vscode': 'Monokai Pro',
        }
    },
}