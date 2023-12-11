from tkinter import *
from tkinter import ttk
 
root = Tk() 
root.geometry("300x500") 
win = Label(root, text ='Web Scrape Top N Recipes', font = "50")  
win.pack()
isVegetarianSelected = IntVar()   
isGlutenFreeSelected = IntVar()   
isNutAllergySelected = IntVar() 

def runWebCrawler():
    INPUT = queryInput.get("1.0", "end-1c")
    output.insert(END, INPUT + ' ')
    output.insert(END, str(isVegetarianSelected.get()) + ' ')
    output.insert(END, str(isGlutenFreeSelected.get()) + ' ')
    output.insert(END, str(isNutAllergySelected.get()) + ' ')
    output.insert(END, '\n')

     
queryLabel = Label(text = "Query")
queryInput = Text(root, height = 5,
                width = 25,
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

queryLabel.pack()
queryInput.pack()  
dietaryRestriction.pack()
vegetarian.pack()   
glutenFree.pack()   
nutAllergy.pack() 
display.pack()
outputLabel.pack()
output.pack()

submit.pack(side = 'bottom')    
  
mainloop()  