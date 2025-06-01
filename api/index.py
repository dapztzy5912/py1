from flask import Flask, jsonify
from personal_intro import IntroductionDisplay

app = Flask(__name__)

@app.route('/')
def show_intro():
    intro = IntroductionDisplay()
    
    data = {
        "name": intro.personal_info.name,
        "title": intro.personal_info.title,
        "age": intro.personal_info.age,
        "location": intro.personal_info.location,
        "email": intro.personal_info.email,
        "phone": intro.personal_info.phone,
        "background": intro.personal_info.background,
        "skills": intro.personal_info.skills,
        "interests": intro.personal_info.interests,
        "website": intro.personal_info.website,
        "linkedin": intro.personal_info.linkedin,
        "github": intro.personal_info.github
    }
    return jsonify(data)
