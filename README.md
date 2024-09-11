## Commands

poetry run task --list

poetry run task lint
OR
task lint


task dbshell
use swgurudb
show collections
db.film.find()


flask --app starwarsguru/app run   # usa .env
pytest                             # usa .env.tests


## URLS

http://localhost:5000/openapi/rapidoc



## LINKS
- https://swapi.dev/
## MONGODB
- https://snyk.io/advisor/python/mongoengine/functions/mongoengine.fields.ListField
- https://docs.mongoengine.org/guide/querying.html
- https://flask.palletsprojects.com/en/2.3.x/patterns/mongoengine/
- http://mongoengine.org/
- https://www.mongodb.com/resources/products/compatibilities/setting-up-flask-with-mongodb
- https://www.mongodb.com/pt-br/docs/manual/reference/database-references/
- https://www.mongodb.com/developer/products/mongodb/cheat-sheet/
## API
- https://luolingchun.github.io/flask-openapi3/latest/Example/#simple-demo


## MONGO QUERIES

```
q2 = Planet.objects.filter(id__in=["66e1e3152fa748ca3839b34c"])

Planet.objects.filter(id__in=["66e1e3152fa748ca3839b34c", "66e1e31b2fa748ca3839b34e"])
    .update(add_to_set__films=['66e1eda75682fd0312c4f0ee'])
Out[13]: 2


# Filtra os planetas que tem o filme 66e21eb69e704403325c1829 e que seja diferene do planeta 2
query = Planet.objects.filter(films__contains='66e21eb69e704403325c1829').filter(id__nin=[str(planet_two.id)])


```