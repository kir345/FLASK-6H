import databases
import sqlalchemy
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('firstname', sqlalchemy.String(60), nullable=False),
    sqlalchemy.Column('lastname', sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column('email', sqlalchemy.String(150), nullable=False),
    sqlalchemy.Column('password', sqlalchemy.String(30), nullable=False),
)

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('prod_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column('descripction', sqlalchemy.String(1000), nullable=True),
    sqlalchemy.Column('price', sqlalchemy.Float, nullable=False),
)

buyes = sqlalchemy.Table(
    'buyes',
    metadata,
    sqlalchemy.Column('buy_id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.user_id'), nullable=False),
    sqlalchemy.Column('prod_id', sqlalchemy.ForeignKey('products.prod_id'), nullable=False),
    sqlalchemy.Column('data', sqlalchemy.Date, nullable=False),
    sqlalchemy.Column('status', sqlalchemy.String(50), nullable=False),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)

metadata.create_all(engine)
