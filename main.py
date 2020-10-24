import requests

presList = ["Washington",
"Adams",
"Jefferson",
"Madison",
"Monroe",
"Adams",
"Jackson",
"Buren",
"Harrison",
"Tyler",
"Polk",
"Taylor",
"Fillmore",
"Pierce",
"Buchanan",
"Lincoln",
"Johnson",
"Grant",
"Hayes",
"Garfield",
"Arthur",
"Cleveland",
"Harrison",
"Cleveland",
"McKinley",
"Roosevelt",
"Taft",
"Wilson",
"Harding",
"Coolidge",
"Hoover",
"Roosevelt",
"Truman",
"Eisenhower",
"Kennedy",
"Johnson",
"Nixon",
"Ford",
"Carter",
"Reagan",
"Bush",
"Clinton",
"Bush",
"Obama",
"Trump", "dummy"]


url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&ia=web&format=json"



def main():
    response = requests.get(url)
    json = response.json()
    for pres in presList:
        presPresent = False
        for key in json["RelatedTopics"]:
            if pres in key["Text"]:
                presPresent = True
        assert presPresent == True




main()







