from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Dish

engine = create_engine('sqlite:///japanesefood.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



# Create dummy user
#user1 = User(name="Mike Robins", email="miker@gmail.com", picture="https://image.flaticon.com/icons/svg/145/145867.svg")
#session.add(user1)
#session.commit()


############### Japanese Rice dishes ###################


category1 = Category(name="Rice Dishes")

session.add(category1)
session.commit()

item1 = Dish(name="Donburi", description="Donburi refers to a bowl of plain cooked rice with some other food on top of it. Donburi are served at specialty restaurants, but they are also a common dish that can be found on all kinds of restaurants' menus. Some of the most popular varieties are gyudon (stewed beef), katsudon (tonkatsu), tendon (tempura), oyakodon (chicken and egg), tekkadon (maguro), and kaisendon (raw seafood).",
                     image="/static/img/donburi.jpg", category=category1)

session.add(item1)
session.commit()


item2 = Dish(name="Curry Rice", description="Kare Raisu (Curry Rice) is cooked rice with a Japanese curry sauce. It can be served with additional toppings such as tonkatsu. Curry is not a native Japanese spice, but has been used in Japan for over a century. Kare Raisu is a very popular dish, and many inexpensive Kare Raisu restaurants can be found especially in and around train stations.",
                     image="/static/img/curryrice.jpg", category=category1)
session.add(item2)
session.commit()


item3 = Dish(name="Onigiri", description="Onigiri, also called omusubi, are known as Japanese rice balls in the West, and are ubiquitous throughout Japan as both a snack and meal accompaniment. Essentially, they’re rice balls with either some kind of filling or ingredients mixed into the rice, and then shaped by hand.",
                     image="/static/img/onigiri.jpg", category=category1)
session.add(item3)
session.commit()


item4 = Dish(name="Omurice", description="Omurice is made exactly like an omelette in that the chicken rice was wrapped in a thin sheet of egg.",
                     image="/static/img/omurice.jpg", category=category1)
session.add(item4)
session.commit()


item5 = Dish(name="Gyudon", description="Gyudon is a Japanese dish consisting of a bowl of rice topped with beef and onion simmered in a mildly sweet sauce flavored with dashi (fish and seaweed stock), soy sauce and mirin.",
                     image="/static/img/gyudon.jpg", category=category1)
session.add(item5)
session.commit()


item6 = Dish(name="Yakimeshi", description="Japanese fried rice, known as “Yakimeshi” in Japan, is such a flavourful and delicious recipe that is super easy to make! It doesn’t require any special ingredients, and you can create it with things you probably already have in your kitchen.",
                     image="/static/img/yakimeshi.jpg", category=category1)
session.add(item6)
session.commit()

item7 = Dish(name="Sushi", description="Sushi is a Japanese dish of specially prepared vinegared rice, usually with some sugar and salt, combined with a variety of ingredients, such as seafood, vegetables, and occasionally tropical fruits.",
                     image="/static/img/sushi.jpg", category=category1)
session.add(item7)
session.commit()

item8 = Dish(name="Hitsumabushi", description="This dish consits of grilled eel on rice.",
                     image="/static/img/hitsumabushi.jpg", category=category1)
session.add(item8)
session.commit()

item9 = Dish(name="Zosui", description="Zōsuiis a mild and thin Japanese rice soup akin to a rice-based vegetable soup. It is made from pre-cooked rice and water seasoned with either soy sauce or miso and cooked with other ingredients such as meat, seafood, mushrooms, and vegetables.",
                     image="/static/img/zosui.jpg", category=category1)
session.add(item9)
session.commit()


############### Seafood dishes ###################

category2 = Category2(name="Seafood Dishes")

session.add(category2)
session.commit()


item1 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item1)
session.commit()

item2 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item2)
session.commit()


item3 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item3)
session.commit()


item4 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item4)
session.commit()


item5 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item5)
session.commit()

item6 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item6)
session.commit()

item7 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item7)
session.commit()

item8 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item8)
session.commit()

item9 = Dish(name="", description=".",
                     image="/static/img/.jpg", category=category2)
session.add(item9)
session.commit()


############### Noodle dishes ###################

############### Nabe dishes ###################

############### Meat fishes ###################

############### Soybean dishes ###################

############### Sweets ###################





print("added japanese food items!")