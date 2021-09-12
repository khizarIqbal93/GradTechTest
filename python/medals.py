medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    #declare a dictionary/object table which will populated in for loop
    table = {}
    #pointsRef is a lookup object. I used this in order to avoid multiple if statements inside for loop
    pointsRef = {
    "1": 3,
    "2": 2,
    "3": 1
    }

    for obj in medalResults:
        #this outer for loop will go through each object
        for x in obj["podium"]:
            #another for loop is used loop through array in object under the key of "podium"
            country = x[2:]
            points = pointsRef[x[0]]
            #this if statement initializes the value of a newly added country to 0
            if not country in table:
                table[country] = 0
            
            # otherwise if country is already in table object, we can add on to the points
            table[country] += points
    
    return table


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
