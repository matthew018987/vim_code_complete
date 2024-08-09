if !has('python3')
    echomsg ':python3 is not available, vim-find-test will not be loaded.'
    finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python3'))
sys.path.insert(0, python_root_dir)
import vim_complete
EOF

let g:sample_python_plugin_loaded = 1

function! Complete(request)
  python3 vim_complete.insert_fn(vim.eval("a:request"))
endfunction

command! -nargs=1 C call Complete(<f-args>)

function! Review()
  let filepath = execute(":echo expand('%:p')")
  python3 vim_complete.review_fn(vim.eval('filepath'))
endfunction

command! -nargs=0 R call Review()
