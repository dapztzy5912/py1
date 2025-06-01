"""
Configuration file for personal introduction information.
"""

class PersonalInfo:
    """Class to store personal information for the introduction display"""
    
    def __init__(self):
        # Basic Information
        self.name = "Your Name Here"
        self.title = "Your Professional Title"
        self.age = "Your Age"
        self.location = "Your City, Country"
        self.email = "your.email@example.com"
        self.phone = "+1234567890"
        
        # Background Information
        self.background = (
            "A brief description about yourself, your education, "
            "work experience, and what drives you professionally."
        )
        
        # Skills and Expertise
        self.skills = [
            "Python Programming",
            "Web Development",
            "Data Analysis",
            "Problem Solving",
            "Team Collaboration",
            "Project Management"
        ]
        
        # Interests and Hobbies
        self.interests = [
            "Technology",
            "Reading",
            "Travel",
            "Photography",
            "Music",
            "Sports"
        ]
        
        # Social and Professional Links
        self.website = "https://yourwebsite.com"
        self.linkedin = "https://linkedin.com/in/yourprofile"
        self.github = "https://github.com/yourusername"
    
    def update_basic_info(self, name=None, title=None, age=None, location=None, 
                          email=None, phone=None):
        """Update basic information"""
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if age is not None:
            self.age = age
        if location is not None:
            self.location = location
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
    
    def update_background(self, background):
        """Update background information"""
        self.background = background
    
    def update_skills(self, skills_list):
        """Update skills list"""
        if isinstance(skills_list, list):
            self.skills = skills_list
        else:
            self.skills = [skill.strip() for skill in skills_list.split(',')]
    
    def update_interests(self, interests_list):
        """Update interests list"""
        if isinstance(interests_list, list):
            self.interests = interests_list
        else:
            self.interests = [interest.strip() for interest in interests_list.split(',')]
