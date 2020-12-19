# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:08:19 2015

@author: win
"""
import string

def is_letter(char):
    """
    Given a character, return true if the character given is a letter, 
    otherwise return false.
    
    Parameters
    ----------
    char :  Character (letter, number, sign...)
    
    Returns
    -------
    True : if the character is a letter.
    False : if the character is not a letter.
    
    Exemple
    -------
    In : is_letter("a"), is_letter("3"), is_letter("."), is_letter("@"),
    is_letter("qw")
    Out : (True, False, False, False, False)
    """
    return char in string.ascii_lowercase
    
    
def is_number(char):
    """
    Given a character, return true if the character given is a number, 
    otherwise return false.
    
    Parameters
    ----------
    char :  Character (letter, number, sign...)
    
    Returns
    -------
    True : if the character is a number.
    False : if the character is not a number.
    
    Exemple
    -------
    In : is_number("2"), is_number("2.3"), is_number("w"), is_number("@"),
    is_number("_")
    Out : (True, True, False, False, False)
    """
    return char in string.digits
    
    
def trans(state, char):
    """
    This function is a part of an automaton that can identify if a series of 
    characters correspond to a correct form of an email address. Given a state
    and a chair, return the next state that correspond.
    
    Parameters
    ----------
    state : number that indicate the state of the automaton.
    chair : a character that the automaton interpret to decide the next state 
    according to the state in that moment. 
    
    Returns
    -------
    int
    The next state that correspond according to the state and the chair given.
    
    Example
    -------
    In:  trans(1, "3"), trans(3, "@"), trans(8, "g"), trans(3, "f"), 
    trans(4, ".")
    Out: (2, 7, -1, 4, 5)
    
    Precondition
    ------------
    state : int, between 1 and 7
    chair : numbers, letters, ".", "-", "_" or "@"
    """
    nextState = -1
    
    if state == 1:
       if is_letter(char) or is_number(char) or char == "." or char == "-" or \
          char == "_":
           nextState = 2
       elif char == "@":
           nextState = 7
           
    elif state == 2:
       if is_letter(char) or is_number(char) or char == "." or char == "-" or \
          char == "_":
            nextState = 2
       elif char == "@":
            nextState = 3
            
    elif state == 3:
       if is_letter(char) or is_number(char) or char == "." or char == "-" or \
          char == "_":
            nextState = 4
       elif char == "@":
            nextState = 7
            
    elif state == 4:
       if is_letter(char) or is_number(char) or char == "-" or char == "_":
            nextState = 4
       elif char == ".":
            nextState = 5
       elif char == "@":
            nextState = 7
            
    elif state == 5:
       if is_letter(char) or is_number(char) or char == "-" or char == "_":
            nextState = 6
       elif char == "@" or char == ".":
            nextState = 7
            
    elif state == 6:
       if is_letter(char) or is_number(char) or char == "-" or char == "_":
            nextState = 6
       elif char == "@":
            nextState = 7
       elif char == ".":
            nextState = 5
            
    elif state == 7:
       if is_letter(char) or is_number(char) or char == "." or char == "-" or \
          char == "_" or char == "@":
            nextState = 7
    return nextState
    
    
def is_email(address):
    """
     Given a series of characters, return if that is good for a e-mail address.
    
    Parameters
    ----------
    address : a series of characters (numbers, letters, ".", "-", "_" or "@")
    
    Returns
    -------
    True : if the series of characters is good for a e-mail address.
    False : if the series of characters is not good for a e-mail address.
    
    Example
    -------
    In : is_email("zoro@sunny.es")
    Out : True
    
    In : is_email("eustass@@onepiece.es")
    Out : False
    
    In : is_email("portgasdace..@fire.es")
    Out : True
    
    In : is_email("luffy.@es")
    Out : False
    """
    state = 1
    for char in address:
        state = trans(state, char)
    return (state == 6)
    
