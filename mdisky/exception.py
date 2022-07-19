#Copyright (c) 2022. telegram.me/ask_admin001



class LinkInvalid(Exception):
    "LinkInvalid is a custom exception class that is raised when a given link is invalid"
    def __init__(self, link, message="Given Link is invalid. It could be either not a valid Mdisk Link or API key is Invalid."):
        self.link = link
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.link} -> {self.message}'