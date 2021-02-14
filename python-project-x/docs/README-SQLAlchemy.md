# Docker

https://www.sqlalchemy.org/

https://docs.sqlalchemy.org/en/latest/core/tutorial.html#inserts-and-updates

https://hackersandslackers.com/flask-sqlalchemy-database-models/

https://hackersandslackers.com/flask-login-user-authentication/

https://hackersandslackers.com/series/build-flask-apps/

https://github.com/toddbirchard/flasklogin-tutorial

Simplifica los workflows de BD
Gestiona la base deatos de forma sencilla
Proporciona un ORM
Permite interacturar con la mayoria de base datos
Existen muchas librerias que permiten utilizar : Flask-SQLAlchemy, Apache Airflow, Pandas


pip3 install sqlalchemy

Trabaja con :


* Engines
* Sessions
* Connections


## Engines

Objeto que contiene informacion sobre la BD objetivo

Permite acciones como :

* Abrir conexiones de BD
* Representar a la BD
* Ejecutar consultas


```bash
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

results = engine.execute([YOUR_QUERY])
for row in results:
    ...
results.close()
```

Utiliza el concepto de URI para establecer la conexion

```bash
[DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
```



## Connection

Objeto que permite persistir una conexión con la base de datos

```bash
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

connection = engine.connect()
result = connection.execute([YOUR_QUERY])

for row in results:
    ...
connection.close()
```

la diferencia entre engine y conection es que se estaria utilizando la misma variable para almacenar los datos que para gestionar la conexión de datos


## Sessions

Objeto que permite añadir, quiutar o desacer cambios

```bash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

session.add()

session.delete()

session.commit()

session.close()


```

Sintaxis básica de consultas 

records = session.query([MODEL_NAME]).[RESULTS_TYPE]()

records = session.query([MODEL_NAME]).\
	    [METHOD_1].\
            [METHOD_2].\
            [RESULTS_TYPE]()

Results_type puede ser : all(), first(), one(). scalar() returns a single value if one exists, None if no values exist, or raises an exception if multiple records are returned.
get([VALUES])

Ejemplo para mostrar los datos

```
records = session.query(Customer).all()
for record in records:
    pp.pprint(record)

records = session.query(Customer).all()
for record in records:
    recordObject = {'name': record.name,
                    'position': record.position,
                    'team_name': record.team.name,
                    'team_city': record.team.city}
    print(recordObject)

records = session.query(Customer).join(Order, Order.customer_id == Customer.id).all()
for record in records:
    recordObject = {'first_name': record.first_name,
                    'last_name': record.last_name,
                    'email': record.email,
                    'preferred_language': record.preferred_language,
                    'join_date': record.join_date,
                    'orders': []}
    for order in record.order:
        order = {'order_price': order.price,
                 'currency':  order.currency,
                 'purchase_date':  order.purchase_date,
                 'product':  order.product}
        recordObject['orders'].append(order)
        pp.pprint(recordObject)

```

Ejemplo para filtros 

```
records = session.query(Customer).filter(Customer.first_name == 'Carl').all()

records = session.query(Customer).filter_by(first_name='Carl').all()

records = session.query(Customer).filter(Customer.first_name.like('J%')).all()

```

## Creacion de modelo

```bash
from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String


class User(db.Model):
    id = Column(Integer,
                primary_key=True)
    username = Column(String(80),
                      unique=True, nullable=False)
    email = Column(String(120),
                   unique=True,
                   nullable=False)
    joined = Column(Datetime,
                    unique=False,
                    nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



```

```bash
newuser = User(
    username='admin',
    email='admin@example.com'
 )
session.add(newuser)
session.commit()

session.delete(newuser)
session.commit()

users = User.query.all()

users = User.query.filter(username='todd').all()

```


Ejemplo para filtros 

```
from sqlalchemy import func


records = session.query(func.count(Customer.first_name)).all()
for record in records:
    print(record)

records = session.query(func.count(distinct(Customer.first_name))).all()
for record in records:
    print(record)

records = session.query(func.count(Customer.first_name)).group_by(Customer.first_name).all()


```


# Ejemplo Basico





```bash
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):
    """Data model example."""
    __tablename__ = "example_table"
    __table_args__ = {"schema": "example"}

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(100),
        nullable=False
    )
    description = Column(
        Text,
        nullable=True
    )
    join_date = Column(
        DateTime,
        nullable=False
    )
    vip = Column(
        Boolean,
        nullable=False
    )
    number = Column(
        Float,
        nullable=False
    )
    data = Column(
        PickleType,
        nullable=False
    )

    def __repr__(self):
        return '<UserModel model {}>'.format(self.id)
```

Ejemplo de aplicacion de lo anterior

```bash
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ


# Create engine
db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(db_uri, echo=True)

# Create All Tables
Base.metadata.create_all(engine)
```

```
-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS example.example_table_id_seq;

-- Table Definition
CREATE TABLE "example"."example_table" (
    "id" int4 NOT NULL DEFAULT nextval('example.example_table_id_seq'::regclass),
    "name" varchar(100) NOT NULL,
    "description" text,
    "join_date" timestamp NOT NULL,
    "vip" bool NOT NULL,
    "number" float8 NOT NULL,
    "data" float8 NOT NULL,
    PRIMARY KEY ("id")
);
```

Añadir un elemento

```bash
user = UserModel(
    name='todd',
    description='im testing this',
    vip=True,
    join_date=datetime.now()
)
session.add(user)
session.commit()
print(user)
```


# Ejemplo de relaciones

```bash
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlayerModel(Base):
    """Data model for players."""
    __tablename__ = "sqlalchemy_tutorial_players"
    __table_args__ = {"schema": "example"}

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    team_id = Column(
        Integer,
        ForeignKey('example.sqlalchemy_tutorial_teams.id'),
        nullable=False
    )
    name = Column(
        String(100),
        nullable=False
    )
    position = Column(
        String(100),
        nullable=False
    )

    # Relationships
    team = relationship("TeamModel")

    def __repr__(self):
        return '<Person model {}>'.format(self.id)


class TeamModel(Base):
    """Data model for teams."""
    __tablename__ = "sqlalchemy_tutorial_teams"
    __table_args__ = {"schema": "example"}

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(100),
        nullable=False
    )
    city = Column(
        String(100),
        nullable=False
    )

    def __repr__(self):
        return '<Team model {}>'.format(self.id)
```

models-py

# Relationships
team = relationship("TeamModel", backref="player")

def join_example():
    records = session.query(PlayerModel).\
    	join(TeamModel, TeamModel.id == PlayerModel.team_id).all()
    for record in records:
        recordObject = {
            'name': record.name,
            'position': record.position,
            'team_name': record.team.name,
            'team_city': record.team.city
        }
        print(recordObject)