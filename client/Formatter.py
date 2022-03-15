from typing import Any
from termcolor import colored, cprint
import pyfiglet


class TextStyle():

    def __init__(self, to_print: str, color: str, background_color: str, bold: bool = False, blink: bool = False, reverse: bool = False, underline: bool = False, center: bool = False) -> None:
        '''
        Available colours and attributes for text formatting;
        Text colors:

            grey
            red
            green
            yellow
            blue
            magenta
            cyan
            white
        Text highlights:

            on_grey
            on_red
            on_green
            on_yellow
            on_blue
            on_magenta
            on_cyan
            on_white
        Attributes:

            bold
            dark
            underline
            blink
            reverse
            concealed
        '''

        super().__init__()

        msg = to_print  # initializing a varaible to hold all changes
        avail_colors: list[str] = ['grey',
                                   'red',
                                   'green',
                                   'yellow',
                                   'blue',
                                   'magenta',
                                   'cyan',
                                   'white']
        avail_attrs: list[str] = ['bold'
                                  'dark'
                                  'underline'
                                  'blink'
                                  'reverse'
                                  'concealed']

        fg_color: str = color if color in avail_colors else 'white'
        bg_color: Any = 'on_'+background_color if background_color in avail_colors else "on_grey"
        # print(bg_color)

        if center:

            msg = self.make_center(msg)

        def check_attrs(x): return f'{x}' if x else ''

        msg = colored(msg, fg_color, bg_color, attrs=[check_attrs('bold'), check_attrs(
            'blink'), check_attrs('reverse'), check_attrs('underline')])

        print(msg)
        pass

    def make_center(self, msg: str) -> str:

        return (f"{' ' * len(msg)}" + msg + f"{' ' * len(msg)}")


# TextStyle("HI i did something atleast", 'white',
#           '', center=False, underline=False, blink=False)


class AsciiArt():

    def __init__(self, text: str, font: str) -> Any:

        print(pyfiglet.figlet_format(text, font))
