from .Class_Base import BASE
import os


def _input_int(msg: str) -> int:
    """
    Method used to int input

    ...

    :param msg: str
            message for input error

    :return i: int
            injected variable
    """

    try:
        i = int(input())
    except ValueError:
        i = None
        print(msg)

    return i


def _input_str(msg: str) -> str:
    """
        Method used to string input

        ...

        :param msg: str
                message for input error

        :return i: str
                injected variable
        """

    try:
        i = str(input())
    except ValueError:
        i = None
        print(msg)

    return i


def _input_float(msg: str) -> float:
    """
    Method used to float input

    ...

    :param msg: str
            message for input error

    :return i: float
            injected variable
    """

    try:
        i = float(input())
    except ValueError:
        i = None
        print(msg)

    return i


Input = {'int': _input_int, 'float': _input_float, 'str': _input_str}


def menu_builder(title: str, opts: dict,
                 fill: str, lat_fill: str, align: str,
                 width: int, repeat: bool, error_msg: str,
                 i_type: str) -> object:
    """

    Menu builder using all parameters, called by class_menu_builder, suggested to be called only on UNIQUE menus

    :param title: str
            Menu title, it will be displayed on top of all
    :param opts: dict
            Options dictionary displayed at menu {option_number : option_name}
    :param fill: str
            Top/Separator/Bottom edge
    :param lat_fill: str
            Side edge
    :param align: str
            Text alignment (^ = center, < = left, > = right)
    :param width: int
            Max width occupied by text
    :param repeat: bool
            Repeat when wrong input
    :param error_msg: str
            Error message when wrong input
    :param i_type: str
            Input type ('integer', 'string', 'float')

    :return Input[i_type]: object
    """

    # Check if attribute is empty or if it isn't instance of expected
    if not fill or not isinstance(fill, str): fill = BASE().static_fill

    # Check if attribute is empty or if it isn't instance of expected
    if not title or not isinstance(title, str): title = BASE().static_title

    # Check if attribute is empty or if it isn't instance of expected
    if not opts or not isinstance(opts, dict): opts = BASE().static_opts

    # Check if attribute is empty or if it isn't instance of expected
    if not lat_fill or not isinstance(lat_fill, str): lat_fill = BASE().static_lat_fill

    # Check if attribute is empty or if it isn't instance of expected
    if not align or not isinstance(align, str): align = BASE().static_align

    # Check if attribute is empty or if it isn't instance of expected
    if not repeat or not isinstance(repeat, bool): repeat = BASE().static_repeat

    # Check if attribute is empty or if it isn't instance of expected
    if not width or not isinstance(width, int): width = BASE().static_width

    # Check if attribute is empty or if it isn't instance of expected
    if not error_msg or not isinstance(error_msg, str): error_msg = BASE().static_error_msg

    # Check if attribute is empty or if it isn't instance of expected
    if not i_type or not isinstance(i_type, str): i_type = BASE().static_i_type

    i = None  # Input

    if repeat:  # Check repeat necessity
        while not i:  # Check wrong inputs
            _build_cli(title, opts, fill, lat_fill, align, width)
            i = Input[i_type](error_msg)
    else:
        _build_cli(title, opts, fill, lat_fill, align, width)
        i = Input[i_type](error_msg)

    return i


def _build_cli(title: str, opts: dict,
               fill: str, lat_fill: str, align: str,
               width: int):
    """
    CLI builder, this is only the print function

    ...

    :parameter
    ----------
    same as Menu_Builder except for:
        not repeat: bool
        not error_msg: str
        not i_type: str
    """

    os.system('cls' if os.name == 'nt' else 'clear')

    # Print Menu Header
    print(f'{"":{fill}{align}{width + (len(lat_fill) * 2)}}')  # Top edge
    print(f'{lat_fill}{title:{align}{width}}{lat_fill}')  # Title
    print(f'{"":{fill}{align}{width + (len(lat_fill) * 2)}}')  # Title/Options Separator

    # Print Menu Option
    for k in opts:  # Go through options
        print(f'{lat_fill}{str(k) + " - " + opts[k]:{align}{width}}{lat_fill}')  # Print options

    # Print Menu Bottom Edge
    print(f'{"":{fill}{align}{width + (len(lat_fill) * 2)}}')  # Bottom edge


def class_menu_builder(clazz: object) -> object:
    """
    Build menu using parameters setup on class

    ...

    :param clazz: object

    :return Input[i_type]: object
    """
    # Check for empty object
    if not clazz:
        clazz = BASE()
    else:

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_fill'):
            setattr(clazz, 'static_fill', BASE().static_fill)
        else:
            if not clazz.static_fill: clazz.static_fill = BASE().static_fill

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_opts'):
            setattr(clazz, 'static_opts', BASE().static_opts)
        else:
            if not clazz.static_opts: clazz.static_opts = BASE().static_opts

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_width'):
            setattr(clazz, 'static_width', BASE().static_width)
        else:
            if not clazz.static_width: clazz.static_width = BASE().static_width

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_title'):
            setattr(clazz, 'static_title', BASE().static_title)
        else:
            if not clazz.static_title: clazz.static_title = BASE().static_title

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_align'):
            setattr(clazz, 'static_align', BASE().static_align)
        else:
            if not clazz.static_align: clazz.static_align = BASE().static_align

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_repeat'):
            setattr(clazz, 'static_repeat', BASE().static_repeat)
        else:
            if not clazz.static_repeat: clazz.static_repeat = BASE().static_repeat

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_i_type'):
            setattr(clazz, 'static_i_type', BASE().static_i_type)
        else:
            if not clazz.static_i_type: clazz.static_i_type = BASE().static_i_type

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_lat_fill'):
            setattr(clazz, 'static_lat_fill', BASE().static_lat_fill)
        else:
            if not clazz.static_lat_fill: clazz.static_lat_fill = BASE().static_lat_fill

        # Check if object has attribute, if not create and insert value, else check if value != None
        if not hasattr(clazz, 'static_error_msg'):
            setattr(clazz, 'static_error_msg', BASE().static_error_msg)
        else:
            if not clazz.static_error_msg: clazz.static_error_msg = BASE().static_error_msg

    # Call builder
    return menu_builder(clazz.static_title,
                        clazz.static_opts,
                        clazz.static_fill,
                        clazz.static_lat_fill,
                        clazz.static_align,
                        clazz.static_width,
                        clazz.static_repeat,
                        clazz.static_error_msg,
                        clazz.static_i_type)
