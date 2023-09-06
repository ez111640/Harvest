from app.models import db, Pin


def seed_pins():
    pin1 = Pin(
        id='1',
        boardId='1',
        url='https://i.pinimg.com/564x/84/89/e6/8489e694ff1e28053ad49deab53e917a.jpg',
        link='https://livelovefruit.com/perennial-vegetables-plant-once-harvest-forever/',
        description="Perennial vegetables - crops you can plant once, and harvest year after year - are relatively rare in the plant food world, but save you tonnes of money!",
        title='Plant Once, Pick Forever! 12 Perennial Vegetables You Need To Plant This Summer'
    )
    pin2 = Pin(
        id='2',
        boardId='2',
        url='https://i.pinimg.com/564x/1d/f6/54/1df65436fc1f83e4a887615956c2df96.jpg',
        link="https://simplelivingcountrygal.com/how-to-grow-pumpkins-for-beginners/",
        description="How to grow pumpkins for beginners. A step-by-step guide that will walk you through how to plant, weeding, pest control, and harvest.",
        title='How to Grow Huge Pumpkins Step-By-Step'
    )
    pin3 = Pin(
        id='3',
        boardId='3',
        url='https://i.pinimg.com/564x/1d/f6/54/1df65436fc1f83e4a887615956c2df96.jpg',
        link="https://simplelivingcountrygal.com/how-to-grow-pumpkins-for-beginners/",
        description="How to grow pumpkins for beginners. A step-by-step guide that will walk you through how to plant, weeding, pest control, and harvest.",
        title='How to Grow Huge Pumpkins Step-By-Step'
    )
    pin4 = Pin(
        id='4',
        boardId='4',
        url='https://i.pinimg.com/564x/33/11/fc/3311fcdb34c75d76aa39912a75e0def7.jpg',
        link="https://homesteadsurvivalsite.com/one-tree-every-homesteader-should-plant/",
        description="Trees are a homesteader\'s best friend. They provide shelter from the sun, wind, and rain. And they often have medicinal properties",
        title='The One Tree That Every Homesteader Should Plant'
    )
    pin5 = Pin(
        id="5",
        boardId="1",
        url="https://i.pinimg.com/564x/c4/1a/b5/c41ab5dc63c0c7cd75a2dbd6ac32125f.jpg",
        link="https://thehomesteadinghippy.com/how-to-build-a-food-forest/",
        description="Permaculture food forests are autopilot gardens that need little human intervention except in the beginning. Here's how to build one.",
        title="How to Build a Food Forest Step by Step"
    )
    pin6 = Pin(
        id="6",
        boardId="2",
        url="https://i.pinimg.com/564x/24/4b/7d/244b7d7bb21aca387849901493fa35d8.jpg",
        link="https://ourstoneyacres.com/7-vegetables-that-can-survive-freezing",
        description="Plant these 7 veggies in your backyard garden and they will survive the freezing temperatures that are sure to come this fall and winter.",
        title="7 Vegetables that can Survive Freezing"
    )
    pin7 = Pin(
        id="7",
        boardId="3",
        url="https://i.pinimg.com/564x/c4/1a/b5/c41ab5dc63c0c7cd75a2dbd6ac32125f.jpg",
        link="https://thehomesteadinghippy.com/how-to-build-a-food-forest/",
        description="Permaculture food forests are autopilot gardens that need little human intervention except in the beginning. Here's how to build one.",
        title="How to Build a Food Forest Step by Step"
    )
    pin8 = Pin(
        id="8",
        boardId="1",
        url="https://i.pinimg.com/564x/b2/9f/2a/b29f2aea3401e0e44036149006c9e703.jpg",
        link="https://brownthumbmama.com/vegetables-plant-october/",
        description="Learn which vegetables to plant in October, plus the best varieties, planting tips, and recipes for your harvest. ",
        title="14 Veggies to Plant in October"
    )
    pin9= Pin (
        id="9",
        boardId="5",
        url="https://i.pinimg.com/564x/49/68/3a/49683a5bbf0ea72f84efa2568b95842a.jpg",
        link="https://bakernine.com/off-grid-solar-greenhouse/?pp=1",
        description="Build your own off grid solar greenhouse. Start being self sufficient by growing year round. ",
        title="Build Your Own Solar Off Grid Greenhouse"
    )
    pin10= Pin (
        id="10",
        boardId="5",
        url="https://i.pinimg.com/564x/26/5b/4e/265b4edbe7897d177426f2b3ab8b4901.jpg",
        link="http://diytotry.com/backyard-pallet-projects-for-todays-homestead/",
        description="Here are a few of our favorite pallet projects to make for the homestead.",
        title="12 Backyard Pallet Projects"
    )
    pin11= Pin (
        id="11",
        boardId="6",
        url="https://i.pinimg.com/564x/26/5b/4e/265b4edbe7897d177426f2b3ab8b4901.jpg",
        link="http://diytotry.com/backyard-pallet-projects-for-todays-homestead/",
        description="Here are a few of our favorite pallet projects to make for the homestead.",
        title="12 Backyard Pallet Projects"
    )
    pin12= Pin (
        id="12",
        boardId="5",
        url="https://i.pinimg.com/564x/a0/ef/98/a0ef984a4928a507f6594a03706a2d1a.jpg",
        link="https://hillsborough-homesteading.com/different-types-of-wood-and-their-uses/?utm_medium=social&utm_source=pinterest&utm_campaign=tailwind_tribes&utm_content=tribes&utm_term=442400526_12228820_357695",
        description="Do you know what type of wood to use for your project? Some woods make better fences, while others are better for building your barn.",
        title="Different Types of Wood and their Uses"
    )
    pin13= Pin (
        id="13",
        boardId="5",
        url="https://i.pinimg.com/564x/61/97/20/61972080d65b8cd62bac76ea55843b2b.jpg",
        link="https://www.beenatreewood.com/sawdust-and-wood-shavings/",
        description="It may be possible that someone is willing to pay you some money for your sawdust or wood shavings, read on to find out more!",
        title="What to do with Sawdust and Wood Shavings"
    )
    pin14= Pin (
        id="14",
        boardId="7",
        url="https://i.pinimg.com/564x/9c/a5/05/9ca505c6d6deac77f6dc18f06b759454.jpg",
        link="https://rootsy.org/how-to-make-money-on-your-homestead-cottage-food-laws/?utm_medium=social&utm_source=pinterest&utm_campaign=tailwind_tribes&utm_content=tribes&utm_term=1050328566_49298046_258197",
        description="Ever wonder just how to make money from your homestead? Cottage Food Laws might just be your answer.",
        title="What beginners need to know about Cottage Laws"
    )
    pin15= Pin (
        id="15",
        boardId="7",
        url="https://www.trialandeater.com/rosemary-bread/?pp=0&epik=dj0yJnU9VlhVaUY0aHVUeVhiZFd6VFd4OHE3a01iZHZWM05RaUEmcD0xJm49RE9VRWlQUDlmZTd3MDB5bXRZX3RUQSZ0PUFBQUFBR1QzNGE0",
        link="https://www.trialandeater.com/wp-content/uploads/2014/02/Rosemary-bread-1.jpg.webp",
        description="Fresh rosemary bread. Not only delicious but will make your kitchen smell wonderful while your herb dough is baking in the oven. Especially great to bake if you have a bunch of fresh rosemary sprigs.",
        title="Fresh Rosemary Bread Recipe"
    )
    pin16= Pin (
        id="16",
        boardId="7",
        url="https://i.pinimg.com/564x/25/32/b9/2532b94757d224ee22acc9ef78a657c3.jpg",
        link="https://homestead-honey.com/garden-inspired-meal-planning/?utm_medium=social&utm_source=pinterest&utm_campaign=tailwind_tribes&utm_content=tribes",
        description="When produce is fresh, we like to simplify our meals and let the garden's bounty shine through with garden-inspired meal planning.",
        title="Garden-Inspired Meal Planning"
    )
    pin17= Pin (
        id="17",
        boardId="8",
        url="https://i.pinimg.com/564x/25/32/b9/2532b94757d224ee22acc9ef78a657c3.jpg",
        link="https://homestead-honey.com/garden-inspired-meal-planning/?utm_medium=social&utm_source=pinterest&utm_campaign=tailwind_tribes&utm_content=tribes",
        description="When produce is fresh, we like to simplify our meals and let the garden's bounty shine through with garden-inspired meal planning.",
        title="Garden-Inspired Meal Planning"
    )
    pin18= Pin (
        id="18",
        boardId="8",
        url="https://i.pinimg.com/564x/1a/3e/10/1a3e100726303b377ed778b8ec4be8ad.jpg",
        link="https://ourhomeandheritage.com/staple-homestead-kitchen-items/",
        description="Every homestead kitchen needs these staple items for easier from-scratch cooking. I could not do without them when I'm preparing meals for my family.",
        title="Staple Homestead Kitchen Items fr rfrom Scratch Cooking"
    )

    db.session.add(pin1)
    db.session.add(pin2)
    db.session.add(pin3)
    db.session.add(pin4)
    db.session.add(pin5)
    db.session.add(pin6)
    db.session.add(pin7)
    db.session.add(pin8)
    db.session.add(pin9)
    db.session.add(pin10)
    db.session.add(pin11)
    db.session.add(pin12)
    db.session.add(pin13)
    db.session.add(pin14)
    db.session.add(pin15)
    db.session.add(pin16)
    db.session.add(pin17)
    db.session.add(pin18)

def undo_pins():
    db.session.execute('TRUNCATE pins RESTART IDENTITY CASCADE;')
    db.session.commit()
