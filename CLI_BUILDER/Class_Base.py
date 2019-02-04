class BASE:
    """
    Class containing default menu configurations

    ...

    :argument :static_title : str
                Default menu title
    :argument :static_opts : str
                Default menu options
    :argument :static_error_msg : str
                Default error message
    :argument :static_lat_fill : str
                Default side edge
    :argument :static_repeat: str
                Default configuration for wrong input
    :argument :static_i_type : str
                Default input type
    :argument :static_align : str
                Default text alignment
    :argument :static_width : str
                Default text width size
    :argument :static_fill : str
                Default Top/Bottom edge & Separator style
    """
    static_title = 'Menu'
    static_opts = {1: 'Create', 2: 'Update', 3: 'List', 4: 'Delete', 0: 'Exit'}
    static_error_msg = 'Wrong input type, please input correctly'
    static_lat_fill = '|'
    static_repeat = False
    static_i_type = 'str'
    static_align = '^'
    static_width = 20
    static_fill = '='
