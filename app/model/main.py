# Database Setup Start

# engine = create_engine('sqlite:///fastapi.db', echo=True)
# Base = declarative_base()
# class School(Base):

#     __tablename__ = "woot"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)  


#     def __init__(self, name):

#         self.name = name    

# if(os.path.isfile('fastapi.db') == False):
#     Base.metadata.create_all(engine)

# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('woot', metadata, autoload=True, autoload_with=engine)

# Database Setup End

# database = ConnectDatabase()
