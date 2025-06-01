from config import PersonalInfo

class IntroductionDisplay:
    def __init__(self):
        self.personal_info = PersonalInfo()
        self.width = 80

    def get_text(self):
        """Return formatted text (if you want to show in CLI style)"""
        lines = []
        lines.append("=" * self.width)
        lines.append(f"Name: {self.personal_info.name}")
        lines.append(f"Title: {self.personal_info.title}")
        lines.append(f"Age: {self.personal_info.age}")
        lines.append(f"Location: {self.personal_info.location}")
        lines.append(f"Email: {self.personal_info.email}")
        lines.append(f"Phone: {self.personal_info.phone}")
        lines.append("=" * self.width)
        return "\n".join(lines)
