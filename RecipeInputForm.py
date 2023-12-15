from tkinter import *
from tkinter import ttk
from web_crawler import rankData

# Create root window
root = Tk() 
root.geometry("300x600") 
root.title("Web Scraper")
win = Label(root, text ='Web Scrape Top N Recipes', font = "50")  
win.pack()

# Init dietary restricions combobox values
isVegetarianSelected = IntVar()
isGlutenFreeSelected = IntVar()
isLatoseIntoleranceSelected = IntVar()
isNutAllergySelected = IntVar()

def runWebCrawler():
    # Build the query
    recipe = recipeInput.get("1.0", "end-1c")
    ingredients = str(ingredientsInput.get("1.0", "end-1c")).split(",")
    query = recipe + ' recipes' + (' vegetarian' if isVegetarianSelected.get() == 1 else '') + (' gluten free' if isGlutenFreeSelected.get() == 1 else '') + (' dairy free' if isLatoseIntoleranceSelected.get() == 1 else '') + (' nut free' if isNutAllergySelected.get() == 1 else '')

    # Display user query
    output.insert(END, query)
    output.insert(END, '\n')

    numRecipes = int(numRecipesInput.get("1.0", "end-1c"))
    # Call the webcrawler
    results = rankData(query, numRecipes, ingredients)
    print(results)

    # Build the popup window to display the results
    displayWin = Toplevel(root)
    displayWin.geometry('700x200')
    displayWin.title('Ranked List Of Results')
    Button(displayWin,
                text='Close',
                command=displayWin.destroy).pack(side="bottom")
    Label(displayWin, text="Click on a row to copy link into your clipboard", font = "40", bg="pink").pack(side="top")
    buildResultTable(displayWin, results)
    displayWin.grab_set()
      
# For the popup window to display results
def buildResultTable(window, results):
    frame = Frame(window)
    frame.pack()

    # Scrollbar
    scroll_bar = Scrollbar(frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    results_table = ttk.Treeview(frame,yscrollcommand=scroll_bar.set)

    results_table.pack()

    scroll_bar.config(command=results_table.yview)
  
    # Define our column
    
    results_table['columns'] = ('rank', 'title', 'link')

    # Format our column
    results_table.column("#0", width=0,  stretch=NO)
    results_table.column("rank",anchor=CENTER, width=80)
    results_table.column("title",anchor=SW,width=200)
    results_table.column("link",anchor=SW,width=500)

    # Create Headings 
    results_table.heading("#0",text="",anchor=CENTER)
    results_table.heading("rank",text="Rank",anchor=CENTER)
    results_table.heading("title",text="Title",anchor=SW)
    results_table.heading("link",text="Link",anchor=SW)
    results_table.bind('<ButtonRelease>', lambda e: copyLink(results_table, e))

    # Add results data 
    rank = 1
    for key, value in results.items():
        results_table.insert(parent='',index='end',iid=(rank-1),text=key,
        values=(rank, value, key))
        rank += 1
    results_table.pack()

# When a row in results_table is clicked, copy the row's link into clipboard
def copyLink(tree, event):
    curItem = tree.focus()
    item = tree.item(curItem)
    print(item)
    root.clipboard_clear()
    root.clipboard_append(item['text'])


################# Build Form for Root Window #######################
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

###### Package Elements Into Root Window ########
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