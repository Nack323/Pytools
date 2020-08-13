# Pytools
some python tools for linux

# retromenu.py
it's a file that contains a function called make_menu(menu) which takes a list of strings, creates a quick menu in the center of the screen, which the user can navegate using the up and down arrows and then when they click enter returns the index of the item in the menu.

``` python
import retromenu

menu = ['item1', 'item 2', 'item3']

selection = retromenu.make_menu(menu)

print(menu[selection])
```
