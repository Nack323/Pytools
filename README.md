# Pytools
some python tools for linux which i will probably use in the future but figured some other people might like. The code is very simple and not at all clean but its better than trying to redo everything every time you want a menu

# retromenu.py
it's a file that contains a function called make_menu(menu) which takes a list of strings, creates a quick menu in the center of the screen, which the user can navegate using the up and down arrows and then when they click enter returns the index of the item in the menu.

``` python
import retromenu

menu = ['item1', 'item 2', 'item3']

selection = retromenu.make_menu(menu)

print(menu[selection])
```
