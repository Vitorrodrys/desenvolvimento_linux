
import crud
import models

def main():

    game_developer = crud.crud_game_developer.create(
        models.GameDeveloper(
            name="teste"
        )
    )
    game = crud.crud_game.create(
        models.Game(
            name="teste",
            game_developer_id=game_developer.id,
            genre="Action",
            description="teste",
            price=100.0,
            game_icone="teste"
        )
    )
    print(game_developer, game)


main()