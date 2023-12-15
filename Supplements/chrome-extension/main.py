from js import document
from datetime import datetime

insert_content = document.getElementById('datetime')
output = document.getElementById('output')
number_restrictions = 0

# insert_content.innerHTML = f"<i>{datetime.now().isoformat()}</i>"

def saveData():
    query_data = document.getElementById('query').value
    dietary_restriction_data = document.querySelectorAll('.dietary_restrictions')
    insert_content.innerHTML = query_data
    
    number_restrictions = 0
    for element in dietary_restriction_data:
        if (element.checked):
            number_restrictions = number_restrictions + 1
    output.innerHTML = number_restrictions
