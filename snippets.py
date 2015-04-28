"""Store and retrieve snippets of text"""
import sys
from docstringargs import cmdline
import logging

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

data = {}

@cmdline
def put(name, snippet):
    """Store a snippet with an associated name.

    name: The name of the snippet
    snippet: The snippet text
    """
    logging.info("Storing({!r}, {!r})".format(name, snippet))
    data[name] = snippet
    return name, snippet

@cmdline
def get(name):
    """Retrieve the snippet with a given name.

    name: The name of the snippet
    """
    logging.error("Retrieving({!r})".format(name))
    return data.get(name)

if __name__ == "__main__":
    print("Result: {!r}".format(cmdline.main()))
