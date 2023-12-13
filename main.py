from node import *
from stack import *
from palindrome import *

@staticmethod
def evens_recursion(start: int, end: int):
    """Recursively finds and displays the even numbers between a specified 
    starting and ending value.

    Args:
        start (int): specified starting value
        end (int): specified ending value
    """
    # Base case: If start exceeds end, stop the recursion
    if start > end:
        return
    
    # If start is even, print it
    if start % 2 == 0:
        print(start, end=" ")

    # Recur with the next number
    evens_recursion(start + 1, end)


def evens(start: int, end: int):
    """Recursively finds and displays the even numbers between a specified 
    starting and ending value.

    Args:
        start (int): specified starting value
        end (int): specified ending value
    """
    # Base case: If start exceeds end, stop the recursion
    if start > end:
        return
    
    # If start is even, print it
    if start % 2 == 0:
        print(start, end=" ")

    # Recur with the next number
    evens(start + 1, end)

def main():

    s = node('A', None)    
    s = node('T', s)
    s = node('N', s)
    s = node('A', s)
    s = node('S', s)
  


    selection = s
    selection = s.getLink()
    print(selection.getData()) # S

    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    selection = s
    print(selection.getData()) # A


    c = node('S', None)    
    c = node('U', c)
    c = node('A', c)
    c = node('L', c)
    c = node('C', c)

    print()
    print(s.getData())
    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())


    s.setLink(c)
    
    print()

    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())
    s = s.getLink()
    print(s.getData())

    print('')

    print(f'LOOP')
    print(evens(-10,10))
    print(f'RECURSION')
    print(evens_recursion(-10,10))
main()


def getPlaindromes():

    check_palindrome = input("Enter ten words seperated by a space")
    print(check_palindrome)

    is_palindrome = stack()
    not_palindrome = stack()

    for each_word in check_palindrome.split():
                
        if palindrome.isPalindrome(each_word):
            is_palindrome.push(each_word)
        else:
            not_palindrome.push(each_word)


    print(f'Is Palindromes: {is_palindrome.getData()}')
    print(f'Is Not Palindromes: {not_palindrome.getData()}')        


getPlaindromes()


