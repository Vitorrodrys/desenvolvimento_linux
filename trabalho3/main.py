
import crud
from models import GameDeveloper

from views import MyApplication


def registry_game_developer():
    if crud.crud_game_developer.get_all():
        return
    game_developers = [
        GameDeveloper(name="Rockstar Games"),
        GameDeveloper(name="Naughty Dog"),
        GameDeveloper(name="CD Projekt Red"),
        GameDeveloper(name="Bethesda Game Studios"),
        GameDeveloper(name="Blizzard Entertainment"),
        GameDeveloper(name="Epic Games"),
        GameDeveloper(name="Valve Corporation"),
        GameDeveloper(name="BioWare"),
        GameDeveloper(name="Insomniac Games"),
        GameDeveloper(name="Ubisoft Montreal"),
        GameDeveloper(name="Remedy Entertainment"),
        GameDeveloper(name="343 Industries"),
        GameDeveloper(name="Obsidian Entertainment"),
        GameDeveloper(name="Mojang Studios"),
        GameDeveloper(name="Larian Studios"),
        GameDeveloper(name="Nintendo"),
        GameDeveloper(name="Capcom"),
        GameDeveloper(name="Square Enix"),
        GameDeveloper(name="Konami"),
        GameDeveloper(name="Bandai Namco Entertainment"),
        GameDeveloper(name="Sega"),
        GameDeveloper(name="FromSoftware"),
        GameDeveloper(name="Atlus"),
        GameDeveloper(name="PlatinumGames"),
        GameDeveloper(name="Koei Tecmo Games"),
        GameDeveloper(name="Level-5"),
        GameDeveloper(name="Game Freak"),
        GameDeveloper(name="Cygames"),
        GameDeveloper(name="Supergiant Games"),
        GameDeveloper(name="Telltale Games"),
    ]
    for developer in game_developers:
        crud.crud_game_developer.create(developer)

def main():

    registry_game_developer()
    app = MyApplication()
    app.run()

main()