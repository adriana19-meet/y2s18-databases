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


add_Name("sushi","article",9)


def query_all_articles(name):
    articles = session.query(
      Knowledge).filter_by(name = name).all()
      
    return articles
print(query_all_articles("adoo"))


def delete_Knowledge(name):


 session.query(Knowledge).filter_by(
       name=name).delete()
 session.commit()

 delete_Knowledge("adoo")

 def delete_article_by_topic(name):
     session.query(Knowledge).filter_by(name = name).delete()
     session.commit()



def delete_all_articles():
    session.query(Knowledge).delete()
    session.commit()


  

def query_article_by_topic():

    article = session.query(Knowledge).filter_by(name = name).all()
    return article



def edit_article_rating():
    topic = input("what's ur fav food?")
    new_one =input ("what's ur highest rate ?")
    article = session.query(Knowledge).filter_by(name = name).all()
    article.rating  = rating
    session.commit()

add_Name("mac","article",8)    






    
        



    
