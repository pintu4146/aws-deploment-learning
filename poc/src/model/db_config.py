from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

# MySQL configuration
MYSQL_USER = 'root'
MYSQL_PASSWORD = '4146'
MYSQL_HOST = 'localhost'  # Change this to your MySQL host if not local
MYSQL_PORT = 3306  # Change this to your MySQL port if not default
MYSQL_DATABASE = 'learning'

# Database URL
SQLALCHEMY_DATABASE_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLAlchemy session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


