Ingredients = {
    "butter"  : ("butter", 118.3),
    "sugar"   : ("sugar", 236.6),
    "vanilla" : ("vanilla", 4.929),
    "eggs"    : ("eggs", 2), # whole eggs
    "cocoa"   : ("cocoa", 118.3),
    "flour"   : ("flour", 118.3)
}
butter_soft = False

bowl = []

def melt(this):
	print("Melting {0}".format(this))
def bake(this, temp):
	print("Baking{0} at {1}".format(this, temp))	
def mix(this):
	print("Mixing {0}".format(this))
def add_to_bowl(ingredient):
	print("Adding {0} to bowl".format(ingredient))
	return bowl.append(ingredient)
	
##Algorithm

if butter_soft ==False:
	melt(Ingredients["butter"][0])
	butter_soft = True 

add_to_bowl(Ingredients["sugar"][0])	
add_to_bowl(Ingredients["butter"][0])

mixing_time = 0
mixing_creamy = False
	
while mixing_creamy == False:
	mix(bowl)
	mixing_time +=1
	if mixing_time ==3:
		mixing_creamy = True
		
add_to_bowl(Ingredients["eggs"][0])	
add_to_bowl(Ingredients["vanilla"][0])

mix(bowl)

add_to_bowl(Ingredients["cocoa"][0])	
add_to_bowl(Ingredients["flour"][0])


mixing_time = 0
well_blended = False
while well_blended == False:
	mix(bowl)
	mixing_time +=1
	if mixing_time ==4:
		well_blended = True

cake_pan = bowl
cooking_time = 30
cooking_temperature = 350

for minute in range (0,30):
	bake(cake_pan,cooking_temperature)
	
print("Cake is done!")