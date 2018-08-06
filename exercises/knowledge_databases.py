from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_Name(name,wikipedia,rating):
    Knowledge_object = Knowledge(
        name= name,
        wikipedia = wikipedia,
        rating = rating)

    session.add(Knowledge_object)
    session.commit()


add_Name("sushi","artical",9)



def query_all_articles(name):
    articles = session.query(
      Knowledge).filter_by(name = name).all()
      
      return articles

print(query_all_articles("adoo")







def query_article_by_topic():
    pass

def delete_article_by_topic():
    pass

def delete_all_articles():
    pass

def edit_article_rating():
    pass
