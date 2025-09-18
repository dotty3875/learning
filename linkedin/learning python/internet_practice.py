import urllib.request # makes http requests
import json # lets us work with JSON code
import xml.dom.minidom

web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Result code:", web_url.getcode()) # provides http result code

data = web_url.read() # gets the http content from the url (basically a GET request)
# print(data)

theJSON = json.loads(data)
print(theJSON["text"]) # works like dictionary, call it's key

doc = xml.dom.minidom.parse("samplexml.xml") # reads an xml document

print(doc.nodeName) # name of the node
print(doc.firstChild.tagName) # first child elements tag name

skills = doc.getElementsByTagName("skill") # gets live node data from "skill"

print("Skill count:",skills.length) # returns len of skills - how many different skills
for skill in skills: # iterates through and prints out the "name" of each skill (key pair)
    print(skill.getAttribute("name"))

new_skill = doc.createElement("skill") # create a new skill
new_skill.setAttribute("name", "jQuery") # named jQuery
doc.firstChild.appendChild(new_skill) # appends the first child element with the new skill 

skills = doc.getElementsByTagName("skill") # needs to be here to "refresh" this variable with the new code

print("Skill count:",skills.length)
for skill in skills:
    print(skill.getAttribute("name"))