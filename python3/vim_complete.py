from completions import Completions

try:
    import vim
except:
    print("No vim module available outside vim")
    pass

completions = Completions()

def insert_fn(request):
    print('...working on it') 
    response_text, tokens_used = completions.do(request)
    #print('tokens used: ', tokens_used, '\n')

    # print row by row on the screen
    if len(response_text) > 0:
        # break up response into list for adding to screen
        response_lines = response_text.split('\n')
        # insert lines into file where cursor is
        nb = vim.current.window.cursor[0]
        for line in response_lines:
            vim.current.buffer.append(line, nb - 1)
    return
