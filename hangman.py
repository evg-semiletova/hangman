import random

HANGMAN_PICS = ['''
    ---+
       |
       |
       |
      ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \   |
       ===''']

words =  '''apple orange banana grape lemon peach mango melon cherry berry kiwi lime pear plum olive coconut papaya fig 
          date nut peach apricot pineapple strawberry raspberry blueberry blackberry tangerine clementine grapefruit 
          mandarin pomegranate watermelon cantaloupe cucumber zucchini avocado tomato potato carrot onion garlic ginger 
          cabbage lettuce spinach kale broccoli cauliflower celery parsley basil dill thyme rosemary sage mint oregano 
          bay nutmeg cinnamon pepper salt sugar honey butter cream milk cheese bread egg flour rice pasta beans peas 
          corn oats barley rye wheat buckwheat quinoa almond walnut peanut cashew pistachio hazelnut brazil pecan 
          sunflower'''.split()

def get_random_words(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

