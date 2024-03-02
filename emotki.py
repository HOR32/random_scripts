from simple_term_menu import TerminalMenu
import pyperclip
import os
emotki = ["•`_´•","(= ФェФ=)","( ╥﹏╥) ノシ","┌П┐(ಠ_ಠ)","~\(≧▽≦)/~","¯\_(ツ)_/¯","(⌐■_■)", "(,,•o•,,)"]

mainMen = TerminalMenu(emotki, title="ascii emotki ^_^")
while True:
    optionsIndex = mainMen.show()
    choice = emotki[optionsIndex]
    pyperclip.copy(choice)
    break
