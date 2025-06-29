import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

# URL_DATABASE = 'mysql+pymysql://root:SugaSensei%402025@localhost:3306/blogapplication'
URL_DATABASE = os.getenv("URL_DATABASE")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()