import time
import curses

def print_menu(scr, selected, menu):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
    h, w = scr.getmaxyx();
    for index, row in enumerate(menu):
        x = w//2 - len(row) // 2
        y = h//2 - len(menu) // 2 + index
        if index == selected%len(menu) :
            scr.attron(curses.color_pair(1))
            scr.addstr(y, x, row)
            scr.attroff(curses.color_pair(1))
        else :
            scr.addstr(y, x,row)
    scr.refresh();

def main(stdscr, menu):
    curses.curs_set(0)
    selection = 0;
    while 1:
        print_menu(stdscr, selection, menu);
        key = stdscr.getch() # get pressed key
        stdscr.clear()
        if key == curses.KEY_UP:
            selection -= 1;
        if key == curses.KEY_DOWN :
            selection += 1;
        if key in [10, 13] :
            return selection%len(menu)
            break;
        stdscr.refresh();
        print_menu(stdscr, selection, menu);

def make_menu(menu):
    return curses.wrapper(main, menu)

if __name__ == '__main__' :
    print(make_menu(['item 1', 'item 2', 'item 3']))

