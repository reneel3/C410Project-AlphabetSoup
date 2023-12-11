from __init__ import *

class RecipeInputForm(BaseWidget):

    def __init__(self):
        super(RecipeInputForm,self).__init__('Recipe Input Form')

        #Definition of the forms fields
        self._query     = ControlText('Query')
        self._dietaryRestrictions = ControlCheckBoxList('Dietary Restrictions')
        self._dietaryRestrictions.value = [('Vegetarian', False) , ('Gluten Free', False), ('Nut Allergy', False)]
        self._button        = ControlButton('Press this button')
        
        #Define the organization of the forms
        self.formset = [ '_query', '_dietaryRestrictions', '_button', ' ']
        #The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        #If you remove the ' ' the forms will occupy the entire window

        #Define the button action
        self._button.value = self.__buttonAction

    def __buttonAction(self):
        """Button action event"""
        from web_crawler import WebCrawler
        WebCrawler.launch_browser()


#Execute the application
if __name__ == "__main__":   pyforms.start_app( RecipeInputForm )