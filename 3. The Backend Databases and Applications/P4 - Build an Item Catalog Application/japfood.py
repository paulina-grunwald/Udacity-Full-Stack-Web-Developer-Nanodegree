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
#user1 = User(name="PaulinaGrunwad", email="paulina.grunwald@gmail.com", picture="https://image.flaticon.com/icons/svg/194/194938.svg")
#session.add(user1)
#session.commit()


############### Japanese Rice dishes ###################


category1 = Category(name="Rice Dishes", user_id=1)

session.add(category1)
session.commit()

item1 = Dish(user_id=1, name="Donburi", description="Donburi refers to a bowl of plain cooked rice with some other food on top of it. Donburi are served at specialty restaurants, but they are also a common dish that can be found on all kinds of restaurants' menus. Some of the most popular varieties are gyudon (stewed beef), katsudon (tonkatsu), tendon (tempura), oyakodon (chicken and egg), tekkadon (maguro), and kaisendon (raw seafood).",
                     image="/static/img/donburi.jpg", category=category1)

session.add(item1)
session.commit()


item2 = Dish(user_id=1, name="Curry Rice", description="Kare Raisu (Curry Rice) is cooked rice with a Japanese curry sauce. It can be served with additional toppings such as tonkatsu. Curry is not a native Japanese spice, but has been used in Japan for over a century. Kare Raisu is a very popular dish, and many inexpensive Kare Raisu restaurants can be found especially in and around train stations.",
                     image="/static/img/curryrice.jpg", category=category1)
session.add(item2)
session.commit()


item3 = Dish(user_id=1, name="Onigiri", description="Onigiri, also called omusubi, are known as Japanese rice balls in the West, and are ubiquitous throughout Japan as both a snack and meal accompaniment. Essentially, they are rice balls with either some kind of filling or ingredients mixed into the rice, and then shaped by hand.",
                     image="/static/img/onigiri.jpg", category=category1)
session.add(item3)
session.commit()


item4 = Dish(user_id=1, name="Omurice", description="Omurice is made exactly like an omelette in that the chicken rice was wrapped in a thin sheet of egg.",
                     image="/static/img/omurice.jpg", category=category1)
session.add(item4)
session.commit()


item5 = Dish(user_id=1, name="Gyudon", description="Gyudon is a Japanese dish consisting of a bowl of rice topped with beef and onion simmered in a mildly sweet sauce flavored with dashi (fish and seaweed stock), soy sauce and mirin.",
                     image="/static/img/gyudon.jpg", category=category1)
session.add(item5)
session.commit()


item6 = Dish(user_id=1, name="Yakimeshi", description="Japanese fried rice, known as Yakimeshi in Japan, is such a flavourful and delicious recipe that is super easy to make! It doesn not require any special ingredients, and you can create it with things you probably already have in your kitchen.",
                     image="/static/img/yakimeshi.jpg", category=category1)
session.add(item6)
session.commit()

item7 = Dish(user_id=1, name="Sushi", description="Sushi is a Japanese dish of specially prepared vinegared rice, usually with some sugar and salt, combined with a variety of ingredients, such as seafood, vegetables, and occasionally tropical fruits.",
                     image="/static/img/sushi.jpg", category=category1)
session.add(item7)
session.commit()

item8 = Dish(user_id=1, name="Hitsumabushi", description="This dish consits of grilled eel on rice.",
                     image="/static/img/hitsumabushi.jpg", category=category1)
session.add(item8)
session.commit()

item9 = Dish(user_id=1, name="Zosui", description="Zosuiis a mild and thin Japanese rice soup akin to a rice-based vegetable soup. It is made from pre-cooked rice and water seasoned with either soy sauce or miso and cooked with other ingredients such as meat, seafood, mushrooms, and vegetables.",
                     image="/static/img/zosui.jpg", category=category1)
session.add(item9)
session.commit()


############### Seafood dishes ###################

category2 = Category(name="Seafood Dishes", user_id=1)

session.add(category2)
session.commit()


item1 = Dish(user_id=1, name="Shrimp Tempura", description="Cooked bits of tempura are either eaten with dipping sauce, salted without sauce, or used to assemble other dishes. Tempura is commonly served with grated daikon and eaten hot immediately after frying.",
                     image="/static/img/shrimp_tempura.jpg", category=category2)
session.add(item1)
session.commit()

item2 = Dish(user_id=1, name="Takoyaki", description="Takoyaki is a ball-shaped Japanese snack made of a wheat flour-based batter and cooked in a special molded pan. It is typically filled with minced or diced octopus (tako), tempura scraps (tenkasu), pickled ginger, and green onion.",
                     image="/static/img/takoyaki.jpg", category=category2)
session.add(item2)
session.commit()


item3 = Dish(user_id=1, name="Seafood Okonomiyaki", description="Okonomiyaki is a Japanese savory pancake containing a variety of ingredients. The name is derived from the word okonomi.",
                     image="/static/img/okonomiyaki.jpg", category=category2)
session.add(item3)
session.commit()


item4 = Dish(user_id=1, name="Ebichiri", description="Ebichiri is grilled shrimp with doubanjiang, which may or may not contain chili peppers (based on which level of spiciness you choose). Originally a Szechuan dish from China, Ebichiri has been modified to fit the Japanese palate.",
                     image="/static/img/ebichiri.jpg", category=category2)
session.add(item4)
session.commit()


item5 = Dish(user_id=1, name="Shiozake ", description="Shiozake (shio=salt, sake/zake=salmon) is grilled, salted salmon that is a very common dish for anytime of the day in Japan.  It is often eaten for breakfast, but also a great item for Bento box for lunch and even a main dish for dinner.",
                     image="/static/img/shiozake.jpg", category=category2)
session.add(item5)
session.commit()

item6 = Dish(user_id=1, name="Buri Daikon", description="Buri Daikon is cooked yellowtail and Daikon radish in a seasoned broth.  This dish is a winter taste in Japan since both main ingredients, yellowtail and Daikon, are in season in winter.",
                     image="/static/img/buridaikon.jpg", category=category2)
session.add(item6)
session.commit()

item7 = Dish(user_id=1, name="Tako Sunomono", description="Tako Sunomono (Octopus Salad) is yet another variation of Sunomono, sliced vegetables soaked in sweet vinegar sauce.  While the Sunomono can be as simple as a small dish of cucumber with some sesame seeds, we often mix in seafood such as Tako (octopus) or crab..",
                     image="/static/img/tako.jpg", category=category2)
session.add(item7)
session.commit()

item8 = Dish(user_id=1, name="Kazunoko", description="Kazunoko is salted herring roe that has been marinated in seasoned Dashi. It is a part of Osechi Ryori, the traditional Japanese New Year feast.  There are many kinds of dishes for Osechi Ryori, but Kazunoko is one of the big three celebration dishes, along with Kuromame (sweet black beans) and Tazukuri.",
                     image="/static/img/kazunoko.jpg", category=category2)
session.add(item8)
session.commit()

item9 = Dish(user_id=1, name="Kaki Fry", description="Kaki Fry is breaded and deep-fried oysters, often eaten with Tonkatsu Sauce, lemon juice, and tartar sauce (or other toppings).  It is a taste of winter when oysters are in season in Japan.",
                     image="/static/img/kaki.jpg", category=category2)
session.add(item9)
session.commit()


############### Noodle dishes ###################
category3 = Category(name="Noodle Dishes", user_id=1)

session.add(category3)
session.commit()


item1 = Dish(user_id=1, name="Yaki Udon", description="Delicious Japanese yaki udon noodle dish with cabbage, onion, pork, shiitake mushrooms, and udon noodles stir fried, flavored with mentsuyu and soy sauce.",
                     image="/static/img/yakiudon.jpg", category=category3)
session.add(item1)
session.commit()

item2 = Dish(user_id=1, name="Ramen", description="is a Japanese dish. It consists of Chinese-style wheat noodles served in a meat or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork.",
                     image="/static/img/ramen.jpg", category=category3)
session.add(item2)
session.commit()

item3 = Dish(user_id=1, name="Yakisoba", description="Yakisoba is a classic Japanese stir fry noodles dish with pork and vegetables, and it is seasoned with a sweet & savory sauce similar to Worcestershire sauce.",
                     image="/static/img/yakisoba.jpg", category=category3)
session.add(item3)
session.commit()


############### Nabe dishes ###################
category4 = Category(name="Nabe Dishes", user_id=1)

session.add(category4)
session.commit()


item1 = Dish(user_id=1, name="Sukiyaki", description="Sukiyaki consists of thinly sliced cuts of meat and vegetables in a sweet soy sauce flavoured soup, and is just as tasty with or without the meat slices.",
                     image="/static/img/sukiyaki.jpg", category=category4)
session.add(item1)
session.commit()

item2 = Dish(user_id=1, name="Shabu Shabu", description="Shabu shabu is one of Japan's most popular hot pot dishes along with Sukiyaki. It consists of raw assorted vegetables, tofu, and paper-thin slices of raw beef (or pork) cooked in kombu dashi (broth).",
                     image="/static/img/shabushabu.jpg", category=category4)
session.add(item2)
session.commit()

item3 = Dish(user_id=1, name="Chanko Nabe", description="Chanko Nabe is a robust hot pot filled with all kinds of vegetables and tons of protein in a rich dashi and chicken broth. This well-balanced meal is traditionally eaten by sumo wrestlers but also enjoyed at home or some restaurants.",
                     image="/static/img/chankonabe.jpg", category=category4)
session.add(item3)
session.commit()


############### Meat fishes ###################

category5 = Category(name="Meat Dishes", user_id=1)

session.add(category5)
session.commit()


item1 = Dish(user_id=1, name="Tonkatsu", description="Tonkatsu is a Japanese food which consists of a breaded, deep-fried pork cutlet.",
                     image="/static/img/tonkatsu2.jpg", category=category5)
session.add(item1)
session.commit()

item2 = Dish(user_id=1, name="Yakitori", description="Yakitori s a Japanese type of skewered chicken. Its preparation involves skewering the meat with kushi, a type of skewer typically made of steel, bamboo, or similar materials. ",
                     image="/static/img/yakitori.jpg", category=category5)
session.add(item2)
session.commit()

item3 = Dish(user_id=1, name="Chicken Karage ", description="Karage is apanese fried chicken is made by marinating bite-size pieces of chicken in sake, soy sauce, ginger and garlic before coating them generously with potato starch. When fried, the starch turns into an ultra crispy shell encasing a flavorful juicy bite of chicken.",
                     image="/static/img/.jpg", category=category5)
session.add(item3)
session.commit()


############### Egg dishes ###################
category6 = Category(user_id=1, name="Egg dishes")

session.add(category6)
session.commit()


item1 = Dish(user_id=1, name="Tamagoyaki", description="Sweet yet savory, Tamagoyaki (Japanese rolled omelette), makes a delightful Japanese breakfast or side dish for your bento lunches.",
                     image="/static/img/tamagoyaki.jpg", category=category6)
session.add(item1)
session.commit()

item2 = Dish(user_id=1, name="Omurice", description="Omurice is an example of yoshoku consisting of an omelette made with fried rice and usually topped with ketchup.",
                     image="/static/img/omurice.jpg", category=category6)
session.add(item2)
session.commit()

item3 = Dish(user_id=1, name="Oyakodon", description="Oyakodon is cooked in one pan where onions, chicken, and egg are simmered in an umami rich dashi-based sauce.",
                     image="/static/img/oyakodon.jpg", category=category6)
session.add(item3)
session.commit()


############### Sushi ###################

category7 = Category(name="Soybean Dishes", user_id=1)

session.add(category5)
session.commit()


item1 = Dish(user_id=1, name="Miso", description="Miso is fermented soybean paste used as a soup base and condiment in many Japanese dishes. Like soy sauce, miso comes in a wide variety of colors (from light to dark) and flavors (from salty to sweet) and with various regional differences.",
                     image="/static/img/miso.jpg", category=category7)
session.add(item1)
session.commit()

item2 = Dish(user_id=1, name="Natto", description="Natto is a traditional Japanese food made from soybeans fermented with Bacillus subtilis var. natto. Some eat it as a breakfast food.",
                     image="/static/img/natto.jpg", category=category7)
session.add(item2)
session.commit()

item3 = Dish(user_id=1, name="Edamame ", description="Edamame  is a preparation of immature soybeans in the pod, found in cuisines with origins in East Asia. The pods are boiled or steamed and may be served with salt. In Japan, they are usually blanched in 4% salt water and not served with salt.",
                     image="/static/img/edamame.jpg", category=category7)
session.add(item3)
session.commit()



############### Ramen ###################

category8 = Category(name="Ramen", user_id=1)

session.add(category8)
session.commit()

item1 = Dish(user_id=1, name="Shoyu  Ramen", description="Shoyu ramen soup is a clear, brown broth flavored with soy sauce (shoyu). The soup is usually made of chicken broth but often contains other meats such as pork, beef or fish depending on the region.",
                     image="/static/img/shoyuramen.jpg", category=category8)
session.add(item1)
session.commit()


item2 = Dish(user_id=1, name="Tonkotsu Ramen", description="Particularly popular around Kyushu, tonkotsu ramen is made of pork bones which have been boiled down until they dissolve into a cloudy white broth. The thick, creamy soup is also often flavored with chicken broth and pork fat.",
                     image="/static/img/tonkatsu.jpg", category=category8)
session.add(item1)
session.commit()


item3 = Dish(user_id=1, name="Miso Ramen", description="Miso Ramen is Ramen noodles in a Miso based soup that was created in Japan in the 1960s. Ramen noodles are originally Chinese style noodles, but it's been changed and improved over the years, and evolved to be our own food.",
                     image="/static/img/mistoramen.jpg", category=category8)
session.add(item3)
session.commit()


############### Sweets ###################
category9 = Category(name="Sweets Dishes", user_id=1)

session.add(category9)
session.commit()

item1 = Dish(user_id=1, name="Mochi", description="Mochi are a fundamental ingredient of Japanese desserts. They are also a dessert on their own. For example, mochi can be toasted and sweetened with a topping such as kinako.",
                     image="/static/img/mochi1.jpg", category=category9)
session.add(item1)
session.commit()


item2 = Dish(user_id=1, name="Dorayaki", description="Dorayaki arepancakes sandwiched together with anko. In many cases, other ingredients such as chestnuts, whipped cream and ice cream are also added to the middle.",
                     image="/static/img/dorayaki.jpg", category=category9)
session.add(item2)
session.commit()


item3 = Dish(user_id=1, name="Dango", description="Dango are chewy Japanese rice dumplings that are often served on a stick. They taste best grilled with a sweet topping. Dango can also be toasted over an open fire like marshmallows.",
                     image="/static/img/dango.jpg", category=category9)
session.add(item3)
session.commit()

print("added japanese food items!")