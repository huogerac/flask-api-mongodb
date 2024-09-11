from unittest.mock import ANY
from bson import ObjectId
from starwarsguru.models.planets import Planet, Film
from starwarsguru.services import films_svc


def test_should_create_relate_the_new_film_inside_existing_planets(db):
    """
    Testa se um novo filme adicionado:
    - i) O novo filme tem os planetas 1 e 3
    - ii) Os planetas 1 e 3 passam a ter o relacionamento com o novo filme
    - iii) planeta 2 nao tem filme relacionado
    """

    # GIVEN THIS PLANETS
    planet_one = Planet.objects.create(name="Planet One", climate="Hard")
    planet_two = Planet.objects.create(name="Planet Two", climate="Hard")
    planet_three = Planet.objects.create(name="Planet Three", climate="Hard")

    # WHEN WE CREATE A NEW FILM
    film_planets = [str(planet_one.id), str(planet_three.id)]
    new_film = films_svc.create_film("Filml with 2 planets", "D", "2024", film_planets)

    # THEN
    # i)
    film_planets_db = [str(item.id) for item in Film.objects.get(id=new_film['id']).planets]
    for planet_id in film_planets:
        assert planet_id in film_planets_db

    # ii)
    for planet_id in film_planets:
        planet_id_from_db = Planet.objects.get(id=planet_id).films[0].id
        assert str(planet_id_from_db) == new_film['id']

    # iii)
    len(Planet.objects.get(id=planet_two.id).films) == 0


def test_should_update_the_relation_from_planet_and_film(db):
    """
    Testa se um filme com 2 planetas for alterado:
    - i) O filme existente com relacionamento com os planetas 1 e 3 passa para ter apenas o planeta 2
    - ii) Remove o filme dos planetas 1 e 3
    - iii) Adiciona o filme no Planeta 2
    """

    # GIVEN THIS PLANETS
    planet_one = Planet.objects.create(name="Planet One", climate="Hard")
    planet_two = Planet.objects.create(name="Planet Two", climate="Hard")
    planet_three = Planet.objects.create(name="Planet Three", climate="Hard")
    film_planets = [str(planet_one.id), str(planet_three.id)]
    new_film = films_svc.create_film("Filml with 2 planets", "D", "2024", film_planets)

    # WHEN WE CREATE A NEW FILM
    new_film_planets = [str(planet_two.id)]
    updated_film = films_svc.update_film(
        new_film['id'],
        new_film['title'],
        new_film['director'],
        new_film['release_date'],
        new_film_planets,
    )

    # THEN
    # i)
    film_planets_db = [str(item.id) for item in Film.objects.get(id=new_film['id']).planets]
    assert film_planets_db == [str(planet_two.id)]

    # ii)
    for planet_id in film_planets:
        films_from_db = Planet.objects.get(id=planet_id).films
        assert len(films_from_db) == 0

    # iii)
    Planet.objects.get(id=str(planet_two.id)).films[0].id == new_film['id']
