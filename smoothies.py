flavor = ['honey', 'sugar', 'chocolate syrup', 'vanilla extract', 'flax seed', 'protein power', 'oats', 'peanut butter', 'coffee', 'maple syrup', 'lemon juice', 'peanuts', 'cocoa powder', 'lime juice', 'almond', 'nutmeg', 'curry', 'cinnamon', 'ginger', 'tapioca pearl', 'chai tea', 'basil', 'molasses', 'cloves', 'mint']
fruits = ['peach', 'mixed berries', 'banana', 'strawberry', 'kiwi', 'pineapple', 'spinach', 'carrot', 'blueberry', 'mango', 'kale', 'avocado', 'grapefruit', 'watermelon', 'zucchini', 'cantaloupe', 'melon', 'yam', 'fig', 'tofu', 'sweet potato', 'grapes', 'orange', 'nectarine', 'apple', 'applesauce', 'cucumber']
additive = ['yogurt', 'milk', 'frozen yogurt', 'orange juice', 'crushed ice', 'skim milk', 'greek yogurt', 'nonfat milk', 'soy milk', 'almond milk', 'ice', 'cream', 'ice cream', 'grape soda', 'pineapple juice', 'coconut milk', 'pumpkin pie filling', 'apple juice', 'vodka', 'rum']
smoothie_ingredients = flavor + fruits + additive

import random
for i in range(5):
	print random.choice(smoothie_ingredients)