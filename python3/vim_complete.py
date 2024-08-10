from completions import Completions

try:
    import vim
except:
    print("No vim module available outside vim")
    pass


completions = Completions()


def _print_to_screen(content):
    """
    Add response to the file on screen

    Args:
        content (str): code to add to file

    Returns:
        none
    """
    if len(content) > 0:
        # break up response into list for adding to screen
        response_lines = content.split('\n')
        # insert lines into file where cursor is
        line_number = vim.current.window.cursor[0]
        for line in response_lines:
            vim.current.buffer.append(line, line_number - 1)
            line_number += 1

    return


def _save_to_file(content, filepath):
    """
    Save response to a file in the same folder as the source

    Args:
        content (str): code to add to file
        filepath (str): path to source code

    Returns:
        string containing path to review file
    """

    reviewfile = ''

    # if response exists, write to file
    if len(content) > 0:
        # break up response into list for adding to screen
        response_lines = content.split('\n')
        # write to file
        reviewfile = filepath.replace('.py', '_review.html')
        with open(reviewfile, 'w') as f:
            for line in response_lines:
                f.write(f"{line}\n")

    return reviewfile


def insert_fn(request):
    """
    Process code completion invocation from user

    Args:
        request (str): request from user

    Returns:
        none
    """

    print('...working on it') 
    response_text, tokens_used = completions.write_code(request)
    #print('tokens used: ', tokens_used, '\n')

    _print_to_screen(response_text)

    return


def review_fn(filepath):
    """
    Process code review invocation from user

    Args:
        filepath (str): file path with file name to open file

    Returns:
        none
    """
    # check file is valid for python review
    filepath = filepath.strip()
    if not filepath.endswith('.py'):
        print('this is not a python file')
        return

    print('...working on it, this will take a minute')
    
    # get code into format for sending to api
    code = ''
    for i, line in enumerate(vim.current.buffer):
        code += line + '\n'
    
    response_text, tokens_used = completions.review_code(code)
    reviewfile = _save_to_file(response_text, filepath)
   
    # show user review is complete 
    print('review complete: ', reviewfile)
    
    return 
