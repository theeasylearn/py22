#concept of arbitrary argument function
def filterVegetables(*items):
    #local variable
    vegetables = [
    "Asparagus", "Artichoke", "Arugula", "Beetroot", "Bell Pepper", "Bok Choy", "Broccoli", "Brussels Sprouts",
    "Cabbage", "Carrot", "Cauliflower", "Celery", "Chard", "Chili Pepper", "Corn", "Cucumber", "Daikon Radish",
    "Drumstick", "Eggplant", "Endive", "Fennel", "Garlic", "Ginger", "Green Bean", "Kale", "Leek", "Lettuce",
    "Mushroom", "Mustard Greens", "Okra", "Onion", "Parsley", "Peas", "Potato", "Pumpkin", "Radish", "Red Cabbage",
    "Ridge Gourd", "Spinach", "Spring Onion", "Sweet Potato", "Tomato", "Turnip", "Zucchini", "Fenugreek Leaves",
    "Bottle Gourd", "Bitter Gourd", "Taro Root", "Cluster Beans", "Ivy Gourd", "Snake Gourd", "Colocasia",
    "Curry Leaves", "Ash Gourd", "Scarlet Gourd", "Pointed Gourd"
    ]
    for item in items:
        if item in vegetables:
            print(item)

filterVegetables("Apple", "Broccoli", "Rice", "Mango", "Carrot", "Wheat", "Pineapple", "Spinach", "Oats", "Tomato",  
"Pear", "Cauliflower", "Quinoa", "Banana", "Bell Pepper", "Barley", "Grapes", "Cabbage", "Millet", "Cherry")
print("**********************************************************************************************************")
filterVegetables("Apple", "Broccoli", "Rice", "Mango", "Carrot", "Wheat", "Pineapple", "Spinach", "Oats", "Tomato",  
"Pear", "Cauliflower", "Quinoa", "Banana", "Bell Pepper", "Barley", "Grapes", "Cabbage", "Millet",  
"Cherry", "Pumpkin", "Strawberry", "Corn", "Peach", "Finger Millet")


 