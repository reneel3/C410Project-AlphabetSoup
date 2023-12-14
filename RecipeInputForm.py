import tkinter
from tkinter import *
from tkinter import ttk
from web_crawler import crepes

root = Tk() 
root.geometry("300x600") 
win = Label(root, text ='Web Scrape Top N Recipes', font = "50")  
win.pack()
isVegetarianSelected = IntVar()
isGlutenFreeSelected = IntVar()
isLatoseIntoleranceSelected = IntVar()
isNutAllergySelected = IntVar()

def runWebCrawler():
    recipe = recipeInput.get("1.0", "end-1c")
    ingredients = str(ingredientsInput.get("1.0", "end-1c"))
    query = recipe + ' recipes' + (' vegetarian' if isVegetarianSelected.get() == 1 else '') + (' gluten free' if isGlutenFreeSelected.get() == 1 else '') + (' dairy free' if isLatoseIntoleranceSelected.get() == 1 else '') + (' nut free' if isNutAllergySelected.get() == 1 else '')

    output.insert(END, query)
    output.insert(END, '\n')

    numRecipes = int(numRecipesInput.get("1.0", "end-1c"))
    print(crepes(query, numRecipes))
    # New window with rank, title, and href link
      
recipeLabel = Label(text = "Desired Recipe")
recipeInput = Text(root, height = 2,
                width = 25,
                bg = "light yellow")

ingredientsLabel = Label(text = "Preferred Ingredients - ex. potatoes, cucumbers")
ingredientsInput = Text(root, height = 3,
                width = 25,
                bg = "light yellow")

numRecipesLabel = Label(text = "Number of recipes desired")
numRecipesInput = Text(root, height = 1,
                width = 5,
                bg = "light yellow")

dietaryRestriction = Label(text = "Dietary Restrictions")
vegetarian = Checkbutton(root, text = "Vegetarian",  
                      variable = isVegetarianSelected, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10) 
  
glutenFree = Checkbutton(root, text = "Gluten Free", 
                      variable = isGlutenFreeSelected, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10) 
  
latoseIntolerance = Checkbutton(root, text = "Latose Intolerance", 
                      variable = isLatoseIntoleranceSelected, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 15) 

nutAllergy = Checkbutton(root, text = "Nut Allergy", 
                      variable = isNutAllergySelected, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10) 
  
outputLabel = Label(text = "Display Input")
output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")

display = Button(root, height = 2,
                 width = 20, 
                 text ="Submit Form",
                 command = lambda:runWebCrawler())

submit = Button(root, text = 'Quit', bd = '5',
                          command = root.destroy) 

recipeLabel.pack()
recipeInput.pack()
numRecipesLabel.pack()
numRecipesInput.pack()
ingredientsLabel.pack()
ingredientsInput.pack()
dietaryRestriction.pack()
vegetarian.pack()   
glutenFree.pack()   
nutAllergy.pack() 
latoseIntolerance.pack()
display.pack()
outputLabel.pack()
output.pack()

submit.pack(side = 'bottom')    
  
mainloop()  