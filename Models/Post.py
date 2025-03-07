from dataclasses import dataclass
import datetime

class Post:
    def __init__(self, creator_name, content, posting_date=None):
        self.creator_name = creator_name
        self.content = content
        self.posting_date = posting_date if posting_date else datetime.datetime.now()