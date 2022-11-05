# This program illustrates why we need to be careful with user input. In one
# instance, we see the API_KEY global variable be exposed. When sanitized,
# it becomes inaccessible.

from string import Template

API_KEY = 'This is my cool API key'


class Error:
    def __init__(self):
        pass


if __name__ == '__main__':
    # User input this string: {error.__init__.__globals__[API_KEY]}
    userInput = input("Input text: ")
    err = Error()

    # This code exposes the global variable
    print(userInput.format(error=err))

    # This sanitized code does not
    print(Template(userInput).substitute(error=err))
