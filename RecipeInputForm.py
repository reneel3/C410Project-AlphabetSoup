from tkinter import *
from tkinter import ttk
from web_crawler import rankData

root = Tk() 
root.geometry("300x600") 
root.title("Web Scraper")
win = Label(root, text ='Web Scrape Top N Recipes', font = "50")  
win.pack()
isVegetarianSelected = IntVar()
isGlutenFreeSelected = IntVar()
isLatoseIntoleranceSelected = IntVar()
isNutAllergySelected = IntVar()

def runWebCrawler():
    recipe = recipeInput.get("1.0", "end-1c")
    ingredients = str(ingredientsInput.get("1.0", "end-1c")).split(",")
    query = recipe + ' recipes' + (' vegetarian' if isVegetarianSelected.get() == 1 else '') + (' gluten free' if isGlutenFreeSelected.get() == 1 else '') + (' dairy free' if isLatoseIntoleranceSelected.get() == 1 else '') + (' nut free' if isNutAllergySelected.get() == 1 else '')

    output.insert(END, query)
    output.insert(END, '\n')

    numRecipes = int(numRecipesInput.get("1.0", "end-1c"))
    results = rankData(query, numRecipes, ingredients)
    print(results)
    displayWin = Toplevel(root)
    displayWin.geometry('700x200')
    displayWin.title('Ranked List Of Results')
    Button(displayWin,
                text='Close',
                command=displayWin.destroy).pack(side="bottom")
    Label(displayWin, text="Click on a row to copy link into your clipboard", font = "40", bg="pink").pack(side="top")
    buildResultTable(displayWin, results)
    displayWin.grab_set()
      
def buildResultTable(window, results):
    game_frame = Frame(window)
    game_frame.pack()

    #scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
  
    #define our column
    
    my_game['columns'] = ('rank', 'title', 'link')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("rank",anchor=CENTER, width=80)
    my_game.column("title",anchor=SW,width=200)
    my_game.column("link",anchor=SW,width=500)

    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("rank",text="Rank",anchor=CENTER)
    my_game.heading("title",text="Title",anchor=SW)
    my_game.heading("link",text="Link",anchor=SW)
    my_game.bind('<ButtonRelease>', lambda e: copyLink(my_game, e))

    #add data 
    rank = 1
    for key, value in results.items():
        my_game.insert(parent='',index='end',iid=(rank-1),text=key,
        values=(rank, value, key))
        rank += 1
    my_game.pack()

def copyLink(tree, event):
    curItem = tree.focus()
    item = tree.item(curItem)
    print(item)
    root.clipboard_clear()
    root.clipboard_append(item['text'])


################# Build Form #######################
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
  
outputLabel = Label(text = "Display Input Query")
output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")

display = Button(root, height = 2,
                 width = 20, 
                 text ="Cook Up Recipes",
                 command = lambda:runWebCrawler())

warningLabel = Label(text = "Cooking up your recipes may take a while...",bg="pink")

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
warningLabel.pack()
display.pack()
outputLabel.pack()
output.pack()

submit.pack(side = 'bottom')    
  
mainloop()  