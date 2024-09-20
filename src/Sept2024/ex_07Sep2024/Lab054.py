"""
#### Abstraction,
- Abstraction in Python is a fundamental concept in object-oriented programming.
- focuses on hiding complex implementation details while exposing only the essential features of an object

Abstraction - Hide the details and show what is required
# hiding other classes

To create an abstract class in Python, you need to:

1. Import the `ABC`  class and the `abstractmethod`  decorator from the `abc`  module.
2. Define a class that inherits from `ABC` .
3. Use the `@abstractmethod`  decorator to define abstract methods.

"""
from abc import abstractmethod


class ReadFromExcel:
    @abstractmethod
    def read_from_excel(self):
        pass

class Browser(ReadFromExcel):

    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def stop_browser(self):
        pass

class TC1(Browser):
    # have to complete the incomplete methods of the previous classes, which is marked as @abstractmethod
    def start_browser(self):
        print("Start the browser")

    def stop_browser(self):
        print("Stop the browser")

    def read_from_excel(self):
        print("read from excel")

    def runTC1(self):
        self.start_browser()
        self.read_from_excel()
        self.stop_browser()

tc1 = TC1()
tc1.runTC1()
