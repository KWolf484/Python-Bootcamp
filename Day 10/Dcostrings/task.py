def format_name(f_name, l_name):
    """Takes 2 arguments (first name and last name) and
     return them in the title case format"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



