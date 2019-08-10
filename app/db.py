import sqlalchemy as sa
from sqlalchemy import create_engine

from app.settings import DB_NAME, DB_USER, DB_PASSWORD

metadata = sa.MetaData()

users = sa.Table('users', metadata,
                 sa.Column('id', sa.Integer, primary_key=True),
                 sa.Column('name', sa.String(255), nullable=False),
                 sa.Column('age', sa.Integer, nullable=False),
                 sa.Column('city', sa.String(255), nullable=False))

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://{db_user}:{db_password}@localhost/{db_name}'.format(
        db_name=DB_NAME,
        db_user=DB_USER,
        db_password=DB_PASSWORD
    ))
    metadata.create_all(engine)

