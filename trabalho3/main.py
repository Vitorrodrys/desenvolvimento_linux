import crud
import models

from views import MyApplication


def registry_game_developer():
    if crud.crud_game_developer.has_data():
        return
    game_developers = [
        models.GameDeveloper(name="Rockstar Games"),
        models.GameDeveloper(name="Naughty Dog"),
        models.GameDeveloper(name="CD Projekt Red"),
        models.GameDeveloper(name="Bethesda Game Studios"),
        models.GameDeveloper(name="Blizzard Entertainment"),
        models.GameDeveloper(name="Epic Games"),
        models.GameDeveloper(name="Valve Corporation"),
        models.GameDeveloper(name="BioWare"),
        models.GameDeveloper(name="Insomniac Games"),
        models.GameDeveloper(name="Ubisoft Montreal"),
        models.GameDeveloper(name="Remedy Entertainment"),
        models.GameDeveloper(name="343 Industries"),
        models.GameDeveloper(name="Obsidian Entertainment"),
        models.GameDeveloper(name="Mojang Studios"),
        models.GameDeveloper(name="Larian Studios"),
        models.GameDeveloper(name="Nintendo"),
        models.GameDeveloper(name="Capcom"),
        models.GameDeveloper(name="Square Enix"),
        models.GameDeveloper(name="Konami"),
        models.GameDeveloper(name="Bandai Namco Entertainment"),
        models.GameDeveloper(name="Sega"),
        models.GameDeveloper(name="FromSoftware"),
        models.GameDeveloper(name="Atlus"),
        models.GameDeveloper(name="PlatinumGames"),
        models.GameDeveloper(name="Koei Tecmo Games"),
        models.GameDeveloper(name="Level-5"),
        models.GameDeveloper(name="Game Freak"),
        models.GameDeveloper(name="Cygames"),
        models.GameDeveloper(name="Supergiant Games"),
        models.GameDeveloper(name="Telltale Games"),
    ]
    for developer in game_developers:
        crud.crud_game_developer.create(developer)


def registry_platforms():
    if crud.crud_platform.has_data():
        return
    platforms = [
        models.Platform(name="PlayStation 4"),
        models.Platform(name="PlayStation 5"),
        models.Platform(name="Xbox One"),
        models.Platform(name="Xbox Series X"),
        models.Platform(name="Nintendo Switch"),
        models.Platform(name="Mobile"),
        models.Platform(name="VR"),
        models.Platform(name="Windows"),
        models.Platform(name="Mac"),
        models.Platform(name="Linux"),
        models.Platform(name="PlayStation 3"),
        models.Platform(name="Xbox 360"),
        models.Platform(name="PlayStation 2"),
        models.Platform(name="PlayStation"),
        models.Platform(name="Xbox"),
        models.Platform(name="Wii"),
        models.Platform(name="Wii U"),
        models.Platform(name="Nintendo DS"),
        models.Platform(name="Nintendo 3DS"),
        models.Platform(name="PlayStation Portable"),
        models.Platform(name="PlayStation Vita"),
        models.Platform(name="Sega Genesis"),
        models.Platform(name="Sega Saturn"),
        models.Platform(name="Dreamcast"),
        models.Platform(name="Game Boy"),
        models.Platform(name="Game Boy Color"),
        models.Platform(name="Game Boy Advance"),
        models.Platform(name="Atari 2600"),
        models.Platform(name="Commodore 64"),
    ]
    for platform in platforms:
        crud.crud_platform.create(platform)


def main():
    registry_game_developer()
    registry_platforms()
    app = MyApplication()
    app.run()


main()
