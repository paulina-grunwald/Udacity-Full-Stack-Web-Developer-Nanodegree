from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
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


############### Japanese dishes ###################

rice_dish = Category1(name="Rice Dishes")

session.add(rice_dish)
session.commit()

item1 = Dish(name="Donburi", description="Donburi refers to a bowl of plain cooked rice with some other food on top of it. Donburi are served at specialty restaurants, but they are also a common dish that can be found on all kinds of restaurants' menus. Some of the most popular varieties are gyudon (stewed beef), katsudon (tonkatsu), tendon (tempura), oyakodon (chicken and egg), tekkadon (maguro), and kaisendon (raw seafood).",
                     image="/static/img/donburi.jpg", category=category1)

session.add(item1)
session.commit()


item2 = Dish(name="Curry Rice", description="Kare Raisu (Curry Rice) is cooked rice with a Japanese curry sauce. It can be served with additional toppings such as tonkatsu. Curry is not a native Japanese spice, but has been used in Japan for over a century. Kare Raisu is a very popular dish, and many inexpensive Kare Raisu restaurants can be found especially in and around train stations.",
                     image="/static/img/curryrice.jpg", category=category1)

session.add(menuItem1)
session.commit()


############### Seafood dishes ###################

############### Noodle dishes ###################

############### Nabe dishes ###################

############### Meat fishes ###################

############### Soybean dishes ###################

############### Sweets ###################





print "added japanese food items!"