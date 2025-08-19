"""
Learning first lessson of cherrypy framework
https://docs.cherrypy.dev/en/latest/intro.html
https://docs.cherrypy.dev/en/latest/tutorials.html
"""

import cherrypy


class HelloWorld:
    """
    This class handles the index page
    """
    @cherrypy.expose
    def index(self):
        """
        index page implementation
        """
        return "Hello World"


if __name__ == "__main__":
    cherrypy.quickstart(HelloWorld())
