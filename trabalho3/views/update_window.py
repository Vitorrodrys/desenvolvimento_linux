from gi.repository import Gtk

import crud
import models

from .default_configs import HEIGTH, WIDTH


class UpdateWindow(Gtk.Window):
    def __mount_combobox_gamedeveloper(self, game: models.Game):
        game_developer_combo = Gtk.ComboBoxText()
        game_developers = crud.crud_game_developer.get_all()
        for developer in game_developers:
            game_developer_combo.append(str(developer.id), developer.name)
        game_developer_combo.set_active(game.game_developer_id)
        return game_developer_combo

    def __mount_combobox_genre(self, game: models.Game):
        game_genre_combo = Gtk.ComboBoxText()
        for index, genre in enumerate(models.GameGenre):
            game_genre_combo.append(str(index), str(genre))
            if genre == game.genre:
                game_genre_combo.set_active(index)
        return game_genre_combo

    def __mount_plataform_combobox(self, game: models.Game):
        platform_combo = Gtk.ComboBoxText()
        platforms = crud.crud_platform.get_all()
        for platform in platforms:
            platform_combo.append(str(platform.id), platform.name)
        platform_combo.set_active(game.platform_id)
        return platform_combo

    def __init__(self, game: models.Game):
        super().__init__(title="Atualizar jogo")
        self.set_default_size(HEIGTH, WIDTH)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(vbox)

        label = Gtk.Label(label="Atualize as informacoes desejadas:")
        vbox.append(label)

        # Entrada de texto para o nome do jogo
        entry = Gtk.Entry()
        entry.set_placeholder_text("Nome do jogo")
        entry.set_text(game.name)
        vbox.append(entry)
        self.__gamename_entry = entry

        # Game Description
        entry = Gtk.Entry()
        entry.set_placeholder_text("Descrição do jogo")
        entry.set_text(game.description)
        vbox.append(entry)
        self.__gamedescription_entry = entry

        # Game priece
        entry = Gtk.Entry()
        entry.set_placeholder_text("Preço do jogo")
        entry.set_text(str(game.price))
        vbox.append(entry)
        self.__gameprice_entry = entry

        # game developer combo box
        game_developer_combo = self.__mount_combobox_gamedeveloper(game)
        vbox.append(game_developer_combo)
        self.__gamedeveloper_combo = game_developer_combo

        # game genre combo box
        game_genre_combo = self.__mount_combobox_genre(game)
        vbox.append(game_genre_combo)
        self.__gamegenre_combo = game_genre_combo

        # platform combo box
        platform_combo = self.__mount_plataform_combobox(game)
        vbox.append(platform_combo)
        self.__platform_combo = platform_combo

        self.__game = game

        # Botão de atualizar
        button_save = Gtk.Button(label="Salvar")
        button_save.connect("clicked", self.on_update_clicked)
        vbox.append(button_save)

    def on_update_clicked(self, button):
        name = self.__gamename_entry.get_text()
        description = self.__gamedescription_entry.get_text()
        price = float(self.__gameprice_entry.get_text())
        developer_id = int(self.__gamedeveloper_combo.get_active_id())
        genre = models.GameGenre(self.__gamegenre_combo.get_active_text())
        self.__game.name = name
        self.__game.description = description
        self.__game.price = price
        self.__game.game_developer_id = developer_id
        self.__game.genre = genre
        crud.crud_game.update(self.__game)
        self.destroy()
