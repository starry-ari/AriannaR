import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), users=users)

# This is the User class that defines everything that will be inputted into the portfolio template
class User:
    def __init__(self, name, pic, about, education, work, hobbies, places):
        self.name = name
        self.pic = pic
        self.about = about
        self.education = education
        self.work = work
        self.hobbies = hobbies
        self.places = places

# Education class is composed of school (school name), grad (graduation date), and major (area of study)
class Education:
    def __init__(self, school, grad, major):
        self.school = school
        self.grad = grad
        self.major = major

# Work class is composed of title (job title), company, and description
class Work:
    def __init__(self, title, company, description):
        self.title = title
        self.company = company
        self.description = description

# Hobbies class is composed of hobby (hobby name), description of the hobby, and img (source to the image)
class Hobbies:
    def __init__(self, hobby, description, img):
        self.hobby = hobby
        self.description = description
        self.img = img

# Map class is compposed of the city and country of the location.
# More information may be needed and so more attributes may be added later on
class Places:
    def __init__(self, city, country):
        self.city = city
        self.country = country


# We've defined all the classes we'll use above, so from here on we'll make instances of the classes to break down a user's data
# and input it into the Jinja template for it to be formatted

Hailey = User("Hailey Moon", \
"./static/img/HaileyPic.png", \
"Hi there! My name is Hailey and I’m from South Korea and Boston, MA. I’m passionate about the intersection of design and computer science, and I’m always looking for opportunities to learn!", \
"education", "work", "hobbies", "places")

Aria = User("Aria Richardson", \
 "./static/img/AriaPic.png", \
 "Hello! My name is Arianna and I am from Bowie, MD! I enjoy coding and creating digital media. I have skills in both graphic design and video production. Nice to meet you!", \
 "education", "work", "hobbies", "places")


# List of users that will be included in this portfolio
users = [Hailey, Aria]